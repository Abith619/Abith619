from odoo import models, fields

#                                           Sign Masters
class customItemCategory(models.Model):
    _name='sign.item.category'
    _description="Item Category Masters"

    name = fields.Char("Name", required=True)

class CustomSignSubstrate(models.Model):
    _name = "sign.substrate"
    _description="Sign Substrate Masters"

    name = fields.Char("Name", required=True)

class SignReflectiveMaterials(models.Model):
    _name='sign.reflective.materials'
    _description="Reflective Material Masters"

    name = fields.Char("Name", required=True)

class ProductShapeCustom(models.Model):
    _name='product.shape'
    _description="Product Shape Masters"

    name = fields.Char("Name", required=True)
    category_id : fields.Many2one = fields.Many2one("sign.item.category", string="Parent")

class CustomSignSize(models.Model):
    _name='sign.size'
    _description="Size Masters"

    name = fields.Char("Name", required=True)

class signUnits(models.Model):
    _name='sign.unit'
    _description="Unit Masters"

    name = fields.Char("Unit", required=True)
#                                               Substrate Value
class CustomSignSubstrateMake(models.Model):
    _name="sign.substrate.make"
    _description="Substrate Make Masters"

    name = fields.Char("Make", required=True)
#                                               Reflective Sheet
class CustomSignReflectiveMake(models.Model):
    _name="sign.reflective.make"
    _description="Reflective Make Masters"

    name = fields.Char("Make", required=True)

class CustomSignColor(models.Model):
    _name='sign.color'
    _description="Sign Color Masters"

    name = fields.Char("Name", required=True)
#                                               Sign Vinyl Master
class SignVinylType(models.Model):
    _name='sign.vinyl.type'
    _description="Vinyl Type Masters"

    name = fields.Char("Type", required=True)

class RoadMarking(models.Model):
    _name='road.marking'
    _description="Road Marking Masters"

    name = fields.Char(string="Name", required=True)

class StudsMaster(models.Model):
    _name='studs.master'
    _description="Studs Masters"

    name = fields.Char(string="Name", required=True)

class CrashBarrier(models.Model):
    _name='crash.barrier'
    _description="Crash Barrier Masters"

    name = fields.Char(string="Name", required=True)

class SubstrateThickness(models.Model):
    _name='substrate.thickness'
    _description="Substrate Thickness Masters"

    name = fields.Char(string="Name", required=True)

class ItemParameters(models.Model):
    _name='item.parameter'
    _description="Item Parameter Masters"

    name = fields.Char(string="Name", required=True)

class SheetSuppliers(models.Model):
    _name='sheet.supplier'
    _description="Sheet Supplier Masters"

    name = fields.Char(string="Name", required=True)

class VinylStickers(models.Model):
    _name='vinyl.sticker'
    _description="Vinyl Sticker Masters"

    name = fields.Char(string="Name", required=True)

class EcFlims(models.Model):
    _name='ec.flim'
    _description="Ec Flim Masters"

    name = fields.Char(string="Name", required=True)

class AluminiumSuppliers(models.Model):
    _name = "aluminium.supplier"
    _description="Aluminium Supplier Masters"

    name = fields.Char(string="Name", required=True)

class ScreenPrinting(models.Model):
    _name='screen.printing'
    _description="Screen Printing Masters"

    name = fields.Char(string="Name", required=True)

class PrintingVendors(models.Model):
    _name='printing.vendor'
    _description="Printing Vendor Masters"

    name = fields.Char(string="Name", required=True)

class SignProcessing(models.Model):
    _name='sign.processing'
    _description="Sign Processing Masters"

    name = fields.Char(string="Name", required=True)

class ProcessingVendors(models.Model):
    _name='processing.vendor'
    _description="Processing Vendor Masters"

    name = fields.Char(string="Name", required=True)

class SteelItems(models.Model):
    _name='steel.item'
    _description="Steel Item Masters"

    name = fields.Char(string="Name", required=True)

class Thickness(models.Model):
    _name='material.thickness'
    _description="Material Thickness Masters"

    name = fields.Char(string="Name", required=True)

class SupportPosts(models.Model):
    _name='support.post'
    _description="Support Post Masters"

    name = fields.Char(string="Name", required=True)
