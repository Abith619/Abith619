from odoo import models,fields,api,modules
import requests
import json
import logging

_logger = logging.getLogger(__name__)

class Contacts(models.Model):
	_inherit = 'res.partner'

	zoho_id = fields.Char("Zoho ID")
	is_zoho = fields.Boolean("Zoho ?")


class ResCompany(models.Model):
	_inherit = 'res.company'

	zoho_username = fields.Char("Zoho username")
	zoho_password = fields.Char("Zoho password")
	organization_id = fields.Char("Organization ID")
	# zoho_url = fields.Char("Zoho URL")
	zoho_token = fields.Char("Token")
	# logfile_path = fields.Char("Log File Path")
	import_contacts = fields.Boolean("Import Contacts")
	export_contacts = fields.Boolean("Export Contacts")

	import_items = fields.Boolean("Import Items")
	export_items = fields.Boolean("Export Items")

	auto_sync = fields.Selection([('yes','Yes'),('no','No')],"Auto Sync ?")
	trigger = fields.Selection([('create','Create'),('edit','Edit'),('create_or_edit','Create or Edit'),('none','None')],string = "Triggers")


	@api.multi
	def generate_authtoken(self):
		users = self.env['res.users'].search([('id','=',self.env.uid)],limit=1)
		for user in users:
			username = user.company_id.zoho_username
			password= user.company_id.zoho_password
			url = "https://accounts.zoho.com/apiauthtoken/nb/create?SCOPE=ZohoBooks/booksapi&EMAIL_ID=%s&PASSWORD=%s" %(username,password)
			response = requests.get(url)
			if response.status_code == 200:
				# print(response.text)
				output = response.text
				auth = output.splitlines()[2]
				final_auth_token = auth.replace('AUTHTOKEN=','')
				print(final_auth_token)
				user.company_id.sudo().write({'zoho_token':final_auth_token})

	@api.multi
	def import_contacts_zoho(self):
		users = self.env['res.users'].search([('id','=',self.env.uid)],limit=1)
		for user in users:
			token= user.company_id.zoho_token
			Organization_Id = user.company_id.organization_id
			url = "https://books.zoho.com/api/v3/contacts?organization_id=%s" %(Organization_Id)
			headers = {"Authorization":"Zoho-authtoken "+token,"Content-Type":"application/x-www-form-urlencoded"}
			response = requests.get(url, headers=headers)
			# _logger.error(response.text)
			if response.status_code == 200:
				decoded = json.loads(response.text)
				contacts = decoded.get('contacts')
				# print(contacts)
				for contact in contacts:
					zoho_contact_id = contact.get('contact_id')
					check_contact = self.env['res.partner'].search([('zoho_id','=',zoho_contact_id)])
					if not check_contact:
						vals = {}
						vals['name'] = contact.get('contact_name')
						vals['zoho_id'] = zoho_contact_id
						vals['is_zoho'] = True
						vals['website'] = contact.get('website')
						if contact.get('contact_type') == 'customer':
							vals['customer'] = True
						if contact.get('contact_type') == 'vendor':
							vals['supplier'] = True
						if contact.get('status') == 'active':
							vals['active'] = True
						if contact.get('status') == 'inactive':
							vals['active'] = False
						vals['email'] = contact.get('email')
						vals['phone'] = contact.get('phone')
						vals['mobile'] = contact.get('mobile')
						create_contact = self.env['res.partner'].create(vals)
						if create_contact:
							_logger.error("Contact Created : "+str(create_contact.id))

					else:
						vals = {}
						vals['name'] = contact.get('contact_name')
						vals['zoho_id'] = zoho_contact_id
						vals['is_zoho'] = True
						vals['website'] = contact.get('website')
						if contact.get('contact_type') == 'customer':
							vals['customer'] = True
						if contact.get('contact_type') == 'vendor':
							vals['supplier'] = True
						if contact.get('status') == 'active':
							vals['active'] = True
						if contact.get('status') == 'inactive':
							vals['active'] = False
						vals['email'] = contact.get('email')
						vals['phone'] = contact.get('phone')
						vals['mobile'] = contact.get('mobile')
						update_contact = check_contact.write(vals)
						_logger.error("Contact Updated ")
				# print(decoded)
		

	@api.multi
	def export_contacts_zoho(self):
		users = self.env['res.users'].search([('id','=',self.env.uid)],limit=1)
		for user in users:
			token= user.company_id.zoho_token
			Organization_Id = user.company_id.organization_id
			contacts = self.env['res.partner'].search(['&',('is_zoho','=',True),('zoho_id','=',False)])
			for contact in contacts:
				headers = {"Authorization":"Zoho-authtoken "+token,"Content-Type":"application/x-www-form-urlencoded"}
				url = "https://books.zoho.com/api/v3/contacts?organization_id=%s" %(Organization_Id)
				payload = 'JSONString={"contact_name":"%s","company_name":"%s"}' %(contact.name,contact.name)
				response = requests.post(url,headers=headers,data=payload)
				# print(response.text)
				# # if response.status_code == 200:
				# print(response.text)
				decoded = json.loads(response.text)
				print(decoded)
				contact_dec = decoded.get('contact')
				# print("_____________________________")
				# print(contact_dec)
				# print("_____________________________")
				contact_id = contact_dec.get('contact_id')
				contact.write({'zoho_id':contact_id})


	@api.multi
	def import_items_zoho(self):
		users = self.env['res.users'].search([('id','=',self.env.uid)],limit=1)
		for user in users:
			token= user.company_id.zoho_token
			Organization_Id = user.company_id.organization_id
			url = "https://books.zoho.com/api/v3/items?organization_id=%s" %(Organization_Id)
			headers = {"Authorization":"Zoho-authtoken "+token,"Content-Type":"application/x-www-form-urlencoded"}
			response = requests.get(url, headers=headers)
			_logger.error(response.text)
			if response.status_code == 200:
				decoded = json.loads(response.text)
				items = decoded.get('items')
			    #print(contacts)
				for item in items:
					zoho_item_id = item.get('item_id')
					check_item = self.env['product.template'].search([('zoho_id','=',zoho_item_id)])
					if not check_item:
						vals = {}
						vals['name'] = item.get('item_name')
						vals['zoho_id'] = zoho_item_id
						vals['is_zoho'] = True
						vals['list_price'] = item.get('rate')
						vals['default_code'] = item.get('sku')
						if item.get('status') == 'active':
							vals['active'] = True
						if item.get('status') == 'inactive':
							vals['active'] = False
						vals['standard_price'] = item.get('purchase_rate')
						
						create_item = self.env['product.template'].create(vals)
						if create_item:
							_logger.error("Item Created : "+str(create_item.id))

					else:
						vals = {}
						vals['name'] = item.get('item_name')
						vals['zoho_id'] = zoho_item_id
						vals['is_zoho'] = True
						vals['list_price'] = item.get('rate')
						vals['default_code'] = item.get('sku')
						if item.get('status') == 'active':
							vals['active'] = True
						if item.get('status') == 'inactive':
							vals['active'] = False
						vals['standard_price'] = item.get('purchase_rate')
						
						update_item = check_item.write(vals)
						_logger.error("Item Updated ")

	@api.multi
	def export_items_zoho(self):
		users = self.env['res.users'].search([('id','=',self.env.uid)],limit=1)
		for user in users:
			token= user.company_id.zoho_token
			Organization_Id = user.company_id.organization_id
			items = self.env['product.template'].search(['&',('is_zoho','=',True),('zoho_id','=',False)])
			for item in items:
				headers = {"Authorization":"Zoho-authtoken "+token,"Content-Type":"application/x-www-form-urlencoded"}
				url = "https://books.zoho.com/api/v3/items?organization_id=%s" %(Organization_Id)
				payload = 'JSONString={"name":"%s","rate":%d,"description":"%s","sku":"%s","purchase_rate":"%d"}' %(item.name,item.list_price,item.name,item.default_code,item.standard_price)
				response = requests.post(url,headers=headers,data=payload)
				decoded = json.loads(response.text)
				print(decoded)
				item_dec = decoded.get('item')
				item_id = item_dec.get('item_id')
				item.write({'zoho_id':item_id})
