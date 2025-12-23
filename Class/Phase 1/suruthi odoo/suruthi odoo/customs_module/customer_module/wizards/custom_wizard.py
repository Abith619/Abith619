from odoo import models, fields

class CustomWizard(models.TransientModel):
    _name = 'custom.wizard'
    _description = 'Custom Wizard'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')   # you used "message", so add this

    def save(self):
        """This method will run when 'Save' button clicked"""
        # Just show the values for now
        print("Wizard Saved:", self.name, self.description)
        return True
