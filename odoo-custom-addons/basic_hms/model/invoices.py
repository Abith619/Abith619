
from odoo import models, fields, api, 


class Pro(models.Model):
    _inherit = 'product.product'

    datas = fields.Char(string = 'STOCK LIST')
    # stock = fields.Char(string = 'STOCK ALERT')
    # pay = fields.Char(string = 'Pending Pay')
    # medicine = fields.Char(string = 'Medicine Alert Follow-Up For Next Month')
    # medicine_medicine = fields.Char(string = 'MEDICINE')
    # dosf = fields.Char(string = 'DOSF')
    # bf_af = fields.Char(string='BF/AF')
    # withs = fields.Char(string = 'WITH?')
    # days = fields.Char(string = 'DAYS')
    # courier = fields.Char(string = 'COURIER')
    # track = fields.Char(string = 'TRACKING')
    # shipping = fields.Char(string= 'SHIPPING LOGISTICS')
    # previous = fields.Char(string='PREVIOUS MONTH FOLLOWUP')
    # graph = fields.Char(string= 'GRAPH ON SALES')


# class account_product(models.Model):
#     _inherit = 'account.invoice'

#     op_medical = fields.Char(string = 'OP MED BILL')
#     ip_medical = fields.Char(string = 'IP MED BILL')
#     insurance = fields.Char(string = 'INSURANCE PAY')
#     payment = fields.Char(string = 'PAYMENT GATEAWAY')
#     daily_exp = fields.Char(string = 'DAILY EXP')
#     seperate = fields.Char(string = 'Seperate Columns')
#     month_exp = fields.Char(string='MONTHLY EXPENSE')
#     graph_for = fields.Char(string = 'GRAPH FOR EXP BASED ON CATEGORIES')
#     gst_data = fields.Char(string = 'GST')
#     loans = fields.Char(string = 'LOANS')
#     credits = fields.Char(string= 'CREDITS')
#     pending = fields.Char(string='PENDING')
