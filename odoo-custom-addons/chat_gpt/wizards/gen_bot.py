from odoo import models, api, fields
from datetime import datetime, timedelta
from odoo.exceptions import  ValidationError

class Generate_bot(models.TransientModel):
    _name = 'create.bot'

    bott = fields.Selection([('yes','Yes'),('no','No')],string='Do You want to Create a Bot',default='yes')
    related_id = fields.Many2one('chat.model', string='Related')
    select_relate = fields.Selection([('role','Roles'),('activity','Activities'),('action','Actions'),
                                      ('module','Modules'),('model','Models'),('field','Fields'),], string='Related Func')

    def save(self):
        if self.bott == 'yes':
            if self.select_relate == 'role':
                for i in self.related_id.roles_line:
                    if i.select_roles == True:
                        if i.roles != ' ':
                            orm = self.env['res.partner'].search([('name','=',i.roles)])
                            if not orm:
                                partner_id = self.env['res.partner'].sudo().create({
                                    'name':i.roles,
                                        })

                                channel_id = self.env['mail.channel'].sudo().create({
                                        'public':'public',
                                        'description':'User Role',
                                        'group_public_id':10,
                                        'name':i.roles,
                                        'channel_partner_ids': [(4,partner_id.id)],
                                    })
                                channel_id.message_post(author_id=partner_id.id,
                                    body=('Hi, How may i help you !'),
                                    subject = 'RASA BOT',
                                    message_type='notification',
                                    subtype_xmlid="mail.mt_comment",
                                    channel_ids=[channel_id.id],
                                    partner_ids=[partner_id.id],
                                    notify_by_email=False,
                                        )
            if self.select_relate == 'activity':
                for i in self.related_id.activity_line:
                    if i.select_activity == True:
                        if i.activity != ' ':
                            orm = self.env['res.partner'].search([('name','=',i.activity)])
                            if not orm:
                                partner_id = self.env['res.partner'].sudo().create({
                                    'name':i.activity,
                                        })

                                channel_id = self.env['mail.channel'].sudo().create({
                                        'public':'public',
                                        'description':'User Role',
                                        'group_public_id':10,
                                        'name':i.activity,
                                        'channel_partner_ids': [(4,partner_id.id)],
                                    })
                                channel_id.message_post(author_id=partner_id.id,
                                    body=('Hi, How may i help you !'),
                                    subject = 'RASA BOT',
                                    message_type='notification',
                                    subtype_xmlid="mail.mt_comment",
                                    channel_ids=[channel_id.id],
                                    partner_ids=[partner_id.id],
                                    notify_by_email=False,
                                        )
            if self.select_relate == 'action':
                for i in self.related_id.action_line:
                    if i.select_activity == True:
                        if i.actions != ' ':
                            orm = self.env['res.partner'].search([('name','=',i.actions)])
                            if not orm:
                                partner_id = self.env['res.partner'].sudo().create({
                                    'name':i.actions,
                                        })

                                channel_id = self.env['mail.channel'].sudo().create({
                                        'public':'public',
                                        'description':'User Role',
                                        'group_public_id':10,
                                        'name':i.actions,
                                        'channel_partner_ids': [(4,partner_id.id)],
                                    })
                                channel_id.message_post(author_id=partner_id.id,
                                    body=('Hi, How may i help you !'),
                                    subject = 'RASA BOT',
                                    message_type='notification',
                                    subtype_xmlid="mail.mt_comment",
                                    channel_ids=[channel_id.id],
                                    partner_ids=[partner_id.id],
                                    notify_by_email=False,
                                        )
            if self.select_relate == 'module':
                for i in self.related_id.response_line:
                    if i.select_models == True:
                        if i.modules_name != ' ':
                            orm = self.env['res.partner'].search([('name','=',i.modules_name)])
                            if not orm:
                                partner_id = self.env['res.partner'].sudo().create({
                                    'name':i.modules_name,
                                        })

                                channel_id = self.env['mail.channel'].sudo().create({
                                        'public':'public',
                                        'description':'User Role',
                                        'group_public_id':10,
                                        'name':i.modules_name,
                                        'channel_partner_ids': [(4,partner_id.id)],
                                    })
                                channel_id.message_post(author_id=partner_id.id,
                                    body=('Hi, How may i help you !'),
                                    subject = 'RASA BOT',
                                    message_type='notification',
                                    subtype_xmlid="mail.mt_comment",
                                    channel_ids=[channel_id.id],
                                    partner_ids=[partner_id.id],
                                    notify_by_email=False,
                                        )
            if self.select_relate == 'model':
                for i in self.related_id.sub_model_line:
                    if i.select_models == True:
                        if i.model_name != ' ':
                            orm = self.env['res.partner'].search([('name','=',i.model_name)])
                            if not orm:
                                partner_id = self.env['res.partner'].sudo().create({
                                    'name':i.model_name,
                                        })

                                channel_id = self.env['mail.channel'].sudo().create({
                                        'public':'public',
                                        'description':'User Role',
                                        'group_public_id':10,
                                        'name':i.model_name,
                                        'channel_partner_ids': [(4,partner_id.id)],
                                    })
                                channel_id.message_post(author_id=partner_id.id,
                                    body=('Hi, How may i help you !'),
                                    subject = 'RASA BOT',
                                    message_type='notification',
                                    subtype_xmlid="mail.mt_comment",
                                    channel_ids=[channel_id.id],
                                    partner_ids=[partner_id.id],
                                    notify_by_email=False,
                                        )
            if self.select_relate == 'field':
                for i in self.related_id.fields_line:
                    if i.select_fields == True:
                        if i.fields_name != ' ':
                            orm = self.env['res.partner'].search([('name','=',i.fields_name)])
                            if not orm:
                                partner_id = self.env['res.partner'].sudo().create({
                                    'name':i.fields_name,
                                        })

                                channel_id = self.env['mail.channel'].sudo().create({
                                        'public':'public',
                                        'description':'User Role',
                                        'group_public_id':10,
                                        'name':i.fields_name,
                                        'channel_partner_ids': [(4,partner_id.id)],
                                    })
                                channel_id.message_post(author_id=partner_id.id,
                                    body=('Hi, How may i help you !'),
                                    subject = 'RASA BOT',
                                    message_type='notification',
                                    subtype_xmlid="mail.mt_comment",
                                    channel_ids=[channel_id.id],
                                    partner_ids=[partner_id.id],
                                    notify_by_email=False,
                                        )

        else:
            pass
        
