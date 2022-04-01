#                           DecoraTors
from odoo_score import api

@api.returns('res.partner')
def afun(self):
    return 

@api.one
def afun(self):
    self.name = 'toto'

@api.multi
def afun(self):
    len(self)

@api.model
def afun(self):
    pass

@api.depends('name', 'an_other_field')
def afun(self):
    pass

@api.onchange('fieldx')
def do_stuff(self):
   if self.fieldx == 'x':
      self.fieldy = 'toto'

