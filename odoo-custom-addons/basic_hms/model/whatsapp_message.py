# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, sql_db, _, tools
from odoo.tools.mimetypes import guess_mimetype
from datetime import datetime
from odoo.tools import pycompat
from odoo.exceptions import UserError
import html2text
from ..klikapi import texttohtml
import requests
import json
import base64
import threading
import time
import logging
import ast
# from numpy import record
_logger = logging.getLogger(__name__)


try:
    import phonenumbers
    from phonenumbers.phonenumberutil import region_code_for_country_code
    _sms_phonenumbers_lib_imported = True

except ImportError:
    _sms_phonenumbers_lib_imported = False
    _logger.info(
        "The `phonenumbers` Python module is not available. "
        "Phone number validation will be skipped. "
        "Try `pip3 install phonenumbers` to install it."
    )
    
class WhatsappComposeMessage(models.TransientModel):
    _name = 'whatsapp.compose.message'
    _description = "Whatsapp Message"

    @api.model
    def _get_composition_mode_selection(self):
        return [('comment', 'Post on a document'),
                ('mass_mail', 'Whatsapp Mass Mailing'),
                ('mass_post', 'Post on Multiple Documents')]
        
    #invoice_ids = fields.Many2many('account.invoice', string='Invoice')
    composition_mode = fields.Selection(selection=_get_composition_mode_selection, string='Composition mode', default='comment')
    partner_ids = fields.Many2many('res.partner', 'whatsapp_compose_message_res_partner_rel',
        'wizard_id', 'partner_id' , string='Contacts')
    subject = fields.Char('Subject')
    message = fields.Text()
    #message_html = fields.Html()
    model = fields.Char('Object')
    attachment_ids = fields.Many2many(
        'ir.attachment', 'whatsapp_compose_message_ir_attachments_rel',
        'wizard_id', 'attachment_id', 'Attachments')
    #url_link = fields.Char('Url')
    location = fields.Boolean('Location')
    partner_address_id = fields.Many2one('res.partner', string='Address')
    lat = fields.Float('Lat')
    long = fields.Float('Long')
    type = fields.Selection([('contact', 'Contacts'),('group', 'Groups')], default='group')
    whatsapp_type = fields.Selection([('post', 'Post'),('get', 'Get')], default='post')
    template_id = fields.Many2one(
        'mail.template', 'Use template', index=True,
        )
    
    @api.multi
    @api.onchange('template_id')
    def onchange_template_id_wrapper(self):
        self.ensure_one()
        res_id = self._context.get('active_id') or 1
        values = self.onchange_template_id(self.template_id.id, self.model, res_id)['value']
        for fname, value in values.items():
            setattr(self, fname, value)
    
    @api.multi
    def onchange_template_id(self, template_id, model, res_id):
        """ - mass_mailing: we cannot render, so return the template values
            - normal mode: return rendered values
            /!\ for x2many field, this onchange return command instead of ids
        """
        if template_id:
            values = self.generate_email_for_composer(template_id, [res_id])[res_id]
        else:
            default_values = self.with_context(default_model=model, default_res_id=res_id).default_get(['model', 'res_id', 'partner_ids', 'message', 'attachment_ids'])
            values = dict((key, default_values[key]) for key in ['subject', 'body', 'partner_ids', 'email_from', 'reply_to', 'attachment_ids', 'mail_server_id'] if key in default_values)
        # This onchange should return command instead of ids for x2many field.
        # ORM handle the assignation of command list on new onchange (api.v8),
        # this force the complete replacement of x2many field with
        # command and is compatible with onchange api.v7
        values = self._convert_to_write(values)
        return {'value': values}
    
    @api.model
    def generate_email_for_composer(self, template_id, res_ids, fields=None):
        """ Call email_template.generate_email(), get fields relevant for
            mail.compose.message, transform email_cc and email_to into partner_ids """
        multi_mode = True
        if isinstance(res_ids, pycompat.integer_types):
            multi_mode = False
            res_ids = [res_ids]

        if fields is None:
            fields = ['subject', 'body_html', 'email_from', 'email_to', 'partner_to', 'email_cc',  'reply_to', 'attachment_ids', 'mail_server_id']
        returned_fields = fields + ['partner_ids', 'attachments']
        values = dict.fromkeys(res_ids, False)
        #print ('===res_ids==',res_ids)
        template_values = self.env['mail.template'].with_context(tpl_partners_only=True).browse(template_id).generate_email(res_ids, fields=fields)
        for res_id in res_ids:
            res_id_values = dict((field, template_values[res_id][field]) for field in returned_fields if template_values[res_id].get(field))
            res_id_values['message'] = html2text.html2text(res_id_values.pop('body_html', ''))
            values[res_id] = res_id_values

        return multi_mode and values or values[res_ids[0]]
    
    def format_amount(self, amount, currency):
        fmt = "%.{0}f".format(currency.decimal_places)
        lang = self.env['res.lang']._lang_get(self.env.context.get('lang') or 'en_US')
 
        formatted_amount = lang.format(fmt, currency.round(amount), grouping=True, monetary=True)\
            .replace(r' ', u'\N{NO-BREAK SPACE}').replace(r'-', u'-\N{ZERO WIDTH NO-BREAK SPACE}')
 
        pre = post = u''
        if currency.position == 'before':
            pre = u'{symbol}\N{NO-BREAK SPACE}'.format(symbol=currency.symbol or '')
        else:
            post = u'\N{NO-BREAK SPACE}{symbol}'.format(symbol=currency.symbol or '')
 
        return u'{pre}{0}{post}'.format(formatted_amount, pre=pre, post=post)
 
    def _phone_get_country(self, partner):
        if 'country_id' in partner:
            return partner.country_id
        return self.env.user.company_id.country_id
# 
    def _msg_sanitization(self, partner, field_name):
        number = partner[field_name]
        if number and _sms_phonenumbers_lib_imported:
            country = self._phone_get_country(partner)
            country_code = country.code if country else None
            try:
                phone_nbr = phonenumbers.parse(number, region=country_code, keep_raw_input=True)
            except phonenumbers.phonenumberutil.NumberParseException:
                return number
            if not phonenumbers.is_possible_number(phone_nbr) or not phonenumbers.is_valid_number(phone_nbr):
                return number
            phone_fmt = phonenumbers.PhoneNumberFormat.E164
            return phonenumbers.format_number(phone_nbr, phone_fmt)
        else:
            return number
#             
    def _get_records(self, model):
        if self.env.context.get('active_domain'):
            records = model.search(self.env.context.get('active_domain'))
        elif self.env.context.get('active_ids'):
            records = model.browse(self.env.context.get('active_ids', []))
        else:
            records = model.browse(self.env.context.get('active_id', []))
        return records    

    @api.model
    def default_get(self, fields):
        result = super(WhatsappComposeMessage, self).default_get(fields)
        context = dict(self._context or {})
        Attachment = self.env['ir.attachment']
        active_model = context.get('active_model')
        active_ids = context.get('active_ids')
        active_id = context.get('active_id')
        msg = result.get('message', '')
        result['message'] = msg
        #=======================================================================
        # UPDATE PATCH
        #=======================================================================
        WhatsappServer = self.env['ir.whatsapp_server']
        whatsapp_id = WhatsappServer.search([('status','=','authenticated')], order='sequence asc', limit=1)
        #print ('==message_response==',ast.literal_eval(str(whatsapp_id.message_response)))
        if whatsapp_id and ast.literal_eval(str(whatsapp_id.message_response)) and len(active_ids) > ast.literal_eval(str(whatsapp_id.message_response))['block_limit']:
            raise UserError(_('Maximum blast message whatsapp is %s.') % str(ast.literal_eval(str(whatsapp_id.message_response))['block_limit']))
        #=======================================================================
        #result['model'] = active_model
        #print ('--active_model--',active_ids)
        #if len(active_ids) > 1:
        #    result['composition_mode'] = 'mass_mail'
        partners = self.env['res.partner']
        if active_model and active_ids and active_model == 'res.partner':
            partners = self.env[active_model].browse(active_ids)
            result['model'] = active_model or 'res.partner'
            result['partner_ids'] = [(6, 0, partners.ids)]
        
        if active_model and active_ids and active_model != 'res.partner':
            active = self.env[active_model].browse(active_id)
            if active_model == 'sale.order.line':                
                if active.order_partner_id:
                    partners = [active.order_partner_id.id]
                    if active.order_partner_id.child_ids:
                        for partner in active.order_partner_id.child_ids:
                            partners += partner
            else:
                if active.partner_id:
                    partners = active.partner_id
                    if active.partner_id.child_ids:
                        for partner in active.partner_id.child_ids:
                            partners += partner
                
            records = self.env[active_model].browse(active_ids)
            is_exists = self.env['ir.attachment']
            for record in records:
                res_name = 'Invoice_' + record.number.replace('/', '_') if active_model == 'account.invoice' else record.name.replace('/', '_')
                domain = [('res_id', '=', record.id), ('name', 'like', res_name + '%'), ('res_model', '=', active_model)] 
                is_attachment_exists = Attachment.search(domain, limit=1)
                if active_model != 'sale.order.line' and not is_attachment_exists:
                    attachments = []
                    if active_model == 'sale.order':
                        template = self.env.ref('sale.email_template_edi_sale')
                    elif active_model == 'account.invoice':
                        template = self.env.ref('account.email_template_edi_invoice')
                    elif active_model == 'purchase.order':
                        if self.env.context.get('send_rfq', False):
                            template = self.env.ref('purchase.email_template_edi_purchase')
                        else:
                            template = self.env.ref('purchase.email_template_edi_purchase_done')
                    elif active_model == 'stock.picking':
                        template = self.env.ref('delivery.mail_template_data_delivery_confirmation')
                    elif active_model == 'account.payment':
                        template = self.env.ref('account.mail_template_data_payment_receipt')
                    elif active_model == 'crm.lead':
                        template = self.env.ref('crm.email_template_opportunity_mail')
                        
                    if not template.report_template:
                        continue
                    report = template.report_template
                    report_service = report.report_name
    
                    if report.report_type not in ['qweb-html', 'qweb-pdf']:
                        raise UserError(_('Unsupported report type %s found.') % report.report_type)
                    res, format = report.render_qweb_pdf([record.id])
                    res = base64.b64encode(res)
                    if not res_name:
                        res_name = 'report.' + report_service
                    ext = "." + format
                    if not res_name.endswith(ext):
                        res_name += ext
                    attachments.append((res_name, res))
                    for attachment in attachments:
                        attachment_data = {
                            'name': attachment[0],
                            'datas_fname': attachment[0],
                            'datas': attachment[1],
                            'type': 'binary',
                            'res_model': active_model,
                            'res_id': active_id,
                        }
                        is_exists += Attachment.create(attachment_data)
                else:
                    is_exists += is_attachment_exists
            result['model'] = active_model or 'res.partner'
            result['attachment_ids'] = [(6, 0, is_exists.ids)]
            #print ('===partners==',partners)
            result['partner_ids'] = [(6, 0, partners.ids)] if partners else []
        return result
    
    def _prepare_mail_message(self, author_id, chat_id, record, model, body, data, subject, partner_ids, attachment_ids, response, status):
        #MailMessage = self.env['mail.message']
        #for active_id in active_ids:
        values = {
            'author_id': author_id,
            'model': model or 'res.partner',
            'res_id': record,#model and self.ids[0] or False,
            'body': body,
            'subject': subject or False,
            'message_type': 'whatsapp',
            'record_name': subject,
            'partner_ids': [(4, pid) for pid in partner_ids],
            'attachment_ids': attachment_ids and [(6, 0, attachment_ids.ids)],
            #'parent_id': parent_id,
            #'subtype_id': subtype_id,
            #'channel_ids': kwargs.get('channel_ids', []),
            #'add_sign': True,
            'whatsapp_method': data['method'],
            'whatsapp_data': data,
            'whatsapp_chat_id': chat_id,
            'whatsapp_response': response,
            'whatsapp_status': status,
        }
        #print ('---_prepare_mail_message---',values)
            #MailMessage += MailMessage.sudo().create(values)
        #MailMessage.sudo().create(values)
        return values

    @api.multi
    def whatsapp_message_post_new(self, KlikApi):
        try:
            new_cr = sql_db.db_connect(self.env.cr.dbname).cursor()
            uid, context = self.env.uid, self.env.context
            message = False
            with api.Environment.manage():
                self.env = api.Environment(new_cr, uid, context)
                MailMessage = self.env['mail.message']
                Partners = self.env['res.partner']
                Countries = self.env['res.country']
                for rec in self:
                    active_model = rec.model                    
                    active_ids = context.get('active_ids') or rec.partner_ids.ids
                    #print ('---rec---',rec,active_model,active_ids)
                    if rec.whatsapp_type == 'post':
                        #SEND MESSAGE
                        #MULTI ATTACHMENT
                        message = rec.message
                        #print ('--message--',message)
                        attachment_new_ids = []
                        if rec.attachment_ids:
                            for attach in rec.attachment_ids:
                                vals = {'filename': attach.datas_fname}
                                mimetype = guess_mimetype(base64.b64decode(attach.datas))
                                if mimetype == 'application/octet-stream':
                                    mimetype = 'video/mp4'
                                str_mimetype = 'data:' + mimetype + ';base64,'
                                attachment = str_mimetype + str(attach.datas.decode("utf-8"))
                                vals.update({'datas': attachment})
                                attachment_new_ids.append(vals)
                        #print ('===DETECT OBJECT===',active_model)
                        for record in self.env[active_model].browse(active_ids):
                            #print ('==FOR PARTNER ONLY==',record)                            
                            origin = link = ''
                            amount_total = 0
                            currency_id = False
                            if active_model != 'res.partner':
                                if active_model == 'sale.order':
                                    link = record.get_link()
                                    origin = record.name
                                    currency_id = record.pricelist_id.currency_id
                                    amount_total = record.amount_total                                    
                                    partner = record.partner_id
                                elif active_model == 'purchase.order':
                                    link = record.get_link()
                                    origin = record.name
                                    currency_id = record.currency_id
                                    amount_total = record.amount_total                                    
                                    partner = record.partner_id
                                elif active_model == 'stock.picking':
                                    link = ''
                                    origin = record.name
                                    currency_id = False
                                    amount_total = 0
                                    partner = record.partner_id
                                elif active_model == 'pos.order':
                                    origin = record.name
                                    currency_id = record.currency_id
                                    amount_total = record.amount_total
                                    partner = record.partner_id
                                elif active_model == 'account.invoice':
                                    link = record.get_link()
                                    origin = record.name
                                    currency_id = record.currency_id
                                    amount_total = record.amount_total
                                    partner = record.partner_id
                            else:
                                partner = record
                            if partner.whatsapp:                                
                                whatsapp = partner._formatting_mobile_number()
                                message_data = {
                                    'method': 'sendMessage',
                                    'phone': whatsapp,
                                    'body': message.replace('_PARTNER_', partner.name),
                                    'origin': origin,
                                    'link': link,
                                }
                                if partner.whatsapp == '0' and partner.chat_id:
                                    message_data.update({'phone': '', 'chatId': partner.chat_id})
                                #print ('===data_message==',data_message)
                                #MESSAGE SENT
                                if message_data['body']:
                                    # data_message = json.dumps(message_data)
                                    # send_message = KlikApi.post_request(method='sendMessage', data=data_message)
                                    send_message = {}
                                    status = 'pending'
                                    # if send_message.get('message')['sent']:
                                    #     status = 'send'
                                    #     _logger.warning('Success to send Message to WhatsApp number %s', whatsapp)
                                    # else:
                                    #     status = 'error'
                                    #     _logger.warning('Failed to send Message to WhatsApp number %s', whatsapp)
                                    # print ('==send_message==',send_message)
                                    chatID = None#send_message.get('chatID')
                                    vals = self._prepare_mail_message(self.env.user.partner_id.id, chatID, record and record.id, active_model, texttohtml.formatHtml(message.replace('_PARTNER_', partner.name)), message_data, rec.subject, [partner.id], [], send_message, status)
                                    MailMessage.sudo().create(vals)
                                    partner.chat_id = chatID
                                    new_cr.commit()
                                #ATTACHMENT SENT
                                if attachment_new_ids:
                                    for att in attachment_new_ids:
                                        message_attach = {
                                            'method': 'sendFile',
                                            'phone': whatsapp,
                                            'body': att['datas'].split(",")[0],
                                            'filename': att['filename'],
                                            'caption': texttohtml.formatHtml(message.replace('_PARTNER_', partner.name)),#att['caption'],
                                            'origin': origin,
                                            'link': link,
                                        }
                                        #SENT ATTAHCMENT
                                        if message_attach['body']:
                                            #data_attach = json.dumps(message_attach)
                                            # #_logger.warning('Failed to send Message to WhatsApp number %s, No attachment found', whatsapp)
                                            # print ('===message_attach===',message_attach)
                                            # send_attach = KlikApi.post_request(method='sendFile', data=data_attach)
                                            # print ('===send_attach==',send_attach)
                                            send_attach = {}
                                            status = 'pending'
                                            # if send_attach.get('message')['sent']:        
                                            #     status = 'send'                
                                            #     _logger.warning('Success to send Attachment to WhatsApp number %s', whatsapp)
                                            # else:
                                            #     status = 'error'
                                            #     _logger.warning('Failed to send Attachment to WhatsApp number %s', whatsapp)                                            
                                            chatID = None#send_attach.get('chatID')
                                            vals = self._prepare_mail_message(self.env.user.partner_id.id, chatID, record and record.id, active_model, '', message_attach, rec.subject, [partner.id], rec.attachment_ids, send_attach, status)
                                            MailMessage.sudo().create(vals)
                                            partner.chat_id = chatID
                                            new_cr.commit()
                    elif rec.whatsapp_type == 'get' and rec.type in ('contact', 'group'):
                        print ('#CREATE GROUP OR CONTACT')
                        dialogs = {}
                        #data_dialog = json.dumps(dialogs)
                        get_dialog = KlikApi.get_request(method='dialogs', data=dialogs)
                        #print ('-get_dialog--',get_dialog)
                        if get_dialog.get('dialogs'):
                            for dialog in get_dialog.get('dialogs'):
                                #print ('---dialog---',dialog)
                                if rec.type == 'contact' and dialog.get('id') and '@c.us' in dialog.get('id'):
                                    ContactsExist = Partners.sudo().search([('chat_id','=',dialog.get('id'))], limit=1)
                                    whatsapp = dialog.get('id').replace('@c.us','')
                                    country = Countries.search([('phone_code','=',whatsapp[:2])], limit=1)
                                    whatsapp_number = '0'+whatsapp[2:]
                                    if not ContactsExist:                                        
                                        vals = {
                                            'name': dialog.get('name'),
                                            'whatsapp': whatsapp_number,
                                            'chat_id': dialog.get('id'),
                                            'whatsapp_type': '@c.us',
                                            'customer': True,
                                            'country_id':country.id,
                                        }
                                        Partners.create(vals)
                                        _logger.warning('Added Whatsapp Contact %s**** to Partner Odoo', whatsapp_number[:5])                                                                 
                                        new_cr.commit()
                                        #time.sleep(3)
                                    else:
                                        for part in ContactsExist:
                                            part.write({'name': dialog.get('name')})       
                                            _logger.warning('Updated Whatsapp Contact %s**** to Partner Odoo', whatsapp_number[:5])                                     
                                            new_cr.commit()
                                            #time.sleep(3)
                                elif rec.type == 'group' and dialog.get('id') and '@g.us'  in dialog.get('id'): 
                                    GroupsExist = Partners.sudo().search([('chat_id','=',dialog.get('id'))], limit=1)
                                    whatsapp = dialog.get('id')
                                    country = Countries.search([('phone_code','=',whatsapp[:2])], limit=1)
                                    if not GroupsExist:                              
                                        vals = {
                                            'name': dialog.get('name'),
                                            'whatsapp': '0',
                                            'chat_id': dialog.get('id'),
                                            'whatsapp_type': '@g.us',
                                            'country_id':country.id,
                                        }
                                        Partners.create(vals)
                                        _logger.warning('Added Whatsapp Group *%s* to Partner Odoo', dialog.get('name'))    
                                        new_cr.commit()
                                        #time.sleep(3)
                                    else:
                                        for part in GroupsExist:
                                            part.write({'name': dialog.get('name')})
                                            _logger.warning('Update Whatsapp Group *%s* to Partner Odoo', dialog.get('name'))    
                                            new_cr.commit()
                                            #time.sleep(3)
        finally:
            self.env.cr.close()


    @api.multi
    def whatsapp_message_post(self):
        """Send whatsapp message via threding."""
        WhatsappServer = self.env['ir.whatsapp_server']
        whatsapp_ids = WhatsappServer.search([('status','=','authenticated')], order='sequence asc')
        # for wserver in whatsapp_ids.filtered(lambda ws: ast.literal_eval(str(ws.message_response))['limit_type'] == 'unlimited'\
        #         or ast.literal_eval(str(ws.message_response))['limit_qty'] >= int(ws.message_counts\
        #         or not ast.literal_eval(str(ws.message_response))['block']\
        #         or ast.literal_eval(str(ws.message_response))['wallet_credit'])):
        for wserver in whatsapp_ids.filtered(lambda ws: not ast.literal_eval(str(ws.message_response))['block']):
            if wserver.status != 'authenticated':
                _logger.warning('Whatsapp Authentication Failed!\nConfigure Whatsapp Configuration in General Setting.')
            #if ast.literal_eval(str(ws.message_response))['block_limit'])
            KlikApi = wserver.klikapi()
            KlikApi.auth()
            thread_start = threading.Thread(target=self.whatsapp_message_post_new(KlikApi))
            thread_start.start()
            break
        return True
