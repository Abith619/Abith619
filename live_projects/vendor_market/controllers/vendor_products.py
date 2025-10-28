import base64, io, logging
from PIL import Image
from PIL.Image import Resampling
from odoo.http import request, Controller, route
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class VendorProductsController(Controller):
    @route('/vendor/products', type='http', auth='public', website=True)
    def vendor_products(self, **kwargs):
        user_id = request.env.user.id
        products = request.env['product.template'].search([])
            # ('vendor_id', '=', request.env.user.partner_id.id)
        return request.render('vendor_market.my_products_page', {'products': products})

    @route(['/my/products/create'], type='http', auth='user', website=True, methods=['POST', 'GET'])
    def create_product(self, **kw):
        if request.httprequest.method == 'POST':
            vals = {
                'name': kw.get('name'),
                'list_price': kw.get('list_price'),
                'categ_id': int(kw.get('categ_id')) if kw.get('categ_id') else False,
                'vendor_ids': request.env.user.partner_id.id,
            }

            # Main image
            image = request.httprequest.files.get('image_1920')
            if image:
                if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    raise UserError("Webp file format is not allowed for Product image, Please try converting the image to Jpg or Png Formats")
                img_bytes = image.read()
                im = Image.open(io.BytesIO(img_bytes))
                im.thumbnail((500, 500), Resampling.LANCZOS)
                buffer = io.BytesIO()
                im.save(buffer, format="PNG")
                buffer.seek(0)
                vals['image_1920'] = base64.b64encode(buffer.read())

            # Create product
            product = request.env['product.template'].sudo().create(vals)

            # Extra gallery images
            extra_images = request.httprequest.files.getlist('extra_images')
            for extra_image in extra_images:
                if extra_image and extra_image.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    img_bytes = extra_image.read()
                    im = Image.open(io.BytesIO(img_bytes))
                    im.thumbnail((500, 500), Resampling.LANCZOS)
                    buffer = io.BytesIO()
                    im.save(buffer, format="PNG")
                    buffer.seek(0)
                    img_b64 = base64.b64encode(buffer.read())

                    request.env['product.image'].sudo().create({
                        'product_tmpl_id': product.id,
                        'image_1920': img_b64,
                        'name': extra_image.filename,
                    })

            return request.redirect('/vendor/products')

        categories = request.env['product.category'].sudo().search([])
        return request.render("vendor_market.create_product_page", {
            'categories': categories,
        })


    @route(['/my/products/<int:product_id>/edit'], type='http', auth='user', website=True, methods=['POST', 'GET'])
    def edit_product(self, product_id, **kw):
        product = request.env['product.template'].sudo().browse(product_id)

        if request.httprequest.method == 'POST':
            vals = {
                'name': kw.get('name'),
                'list_price': kw.get('list_price'),
                'categ_id': int(kw.get('categ_id')) if kw.get('categ_id') else False,
            }

            image = kw.get('image_1920')
            if image and not image.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                raise UserError("Webp file format is not allowed for Product image, Please try converting the image to Jpg or Png Formats")
            if image:
                filename = image.filename.lower()

                img_bytes = image.read()

                _logger.info(type(img_bytes))
                # Open with Pillow
                with Image.open(io.BytesIO(img_bytes)) as img:
                    # If it's WebP, convert to JPEG
                    if filename.endswith('.webp'):
                        img = img.convert("RGB")  # JPEG doesn’t support alpha
                        buffer = io.BytesIO()
                        img.save(buffer, format="JPEG", quality=95)
                        buffer.seek(0)
                        img_bytes = buffer.read()
                    else:
                        # Convert any format to standard RGB for consistency
                        img = img.convert("RGB")
                        buffer = io.BytesIO()
                        img.save(buffer, format="JPEG", quality=95)
                        buffer.seek(0)
                        img_bytes = buffer.read()

                vals['image_1920'] = base64.b64encode(img_bytes)

                product.write(vals)

            extra_images = request.httprequest.files.getlist('extra_images')
            for extra_image in extra_images:
                if not extra_image and extra_image.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    raise UserError("Webp file format is not allowed for Product image, Please try converting the image to Jpg or Png Formats")
                if extra_image:
                    img_bytes = extra_image.read()
                    im = Image.open(io.BytesIO(img_bytes))
                    im.thumbnail((500, 500), Resampling.LANCZOS)
                    buffer = io.BytesIO()
                    im.save(buffer, format="PNG")
                    buffer.seek(0)
                    img_b64 = base64.b64encode(buffer.read())

                    uploads = request.env['product.image'].sudo().create({
                        'product_tmpl_id': product.id,
                        'image_1920': img_b64,
                        'name': extra_image.filename,
                    })
                    if uploads:
                        request.session['edit_product_success'] = "Product updated successfully!"
            for variant in product.product_variant_ids:
                qty_field = f"variant_qty_{variant.id}"
                if variant:
                    _logger.info(f"Processing field: {qty_field}")
                    new_qty = float(kw.get(qty_field, 0))

                    stock_location = request.env.ref('stock.stock_location_stock')
                    quant = request.env['stock.quant'].sudo().search([
                        ('product_id', '=', variant.id),
                        ('location_id', '=', stock_location.id),
                    ], limit=1)

                    if quant:
                        quant.sudo().quantity = new_qty
                    else:
                        request.env['stock.quant'].sudo().create({
                            'product_id': variant.id,
                            'location_id': stock_location.id,
                            'quantity': new_qty,
                        })

            return request.redirect('/vendor/products')

        return request.render("vendor_market.edit_product_page", {
            'product': product,
            'gallery': product.product_template_image_ids,
        })

    @route(['/my/products/<int:product_id>/delete'], type='http', auth='user', website=True)
    def delete_product(self, product_id, **kw):
        product = request.env['product.template'].sudo().browse(product_id)
        product.unlink()
        return request.redirect('/my/products')

    @route(['/my/products/<int:product_id>/delete_image/<int:image_id>'], type='http', auth='user', website=True)
    def delete_product_image(self, product_id, image_id, **kw):
        product = request.env['product.template'].sudo().browse(product_id)
        image = request.env['product.image'].sudo().browse(image_id)

        if image and image.product_tmpl_id.id == product.id:
            image.unlink()

        return request.redirect('/my/products/%s/edit' % product_id)
