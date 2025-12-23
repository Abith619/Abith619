from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo import _logger


class CustomUber(models.Model):
    _name = 'custom.uber'
    _description = 'Travelling'

    name = fields.Char("Name")
    age = fields.Integer("Age")
    email = fields.Char("Email")

    price = fields.Float("Price")
    quantity = fields.Integer("Quantity")
    total = fields.Float("Total", compute="_compute_total", store=True)

    message = fields.Char("Message")

    # ----------------------------
    # 1️⃣ @api.model
    # ----------------------------
    @api.model
    def say_hello(self):
        print("Hello da! This is @api.model")

    # ----------------------------
    # 2️⃣ @api.model_create_multi
    # ----------------------------
    @api.model_create_multi
    def create(self, vals_list):
        print("Creating records:", vals_list)
        return super(CustomUber, self).create(vals_list)

    # ----------------------------
    # 3️⃣ @api.onchange
    # ----------------------------
    @api.onchange('age')
    def onchange_age(self):
        if self.age:
            if self.age < 18:
                self.message = "Minor"
            else:
                self.message = "Adult"

    # ----------------------------
    # 4️⃣ @api.depends
    # ----------------------------
    @api.depends('price', 'quantity')
    def _compute_total(self):
        for record in self:
            record.total = (record.price or 0) * (record.quantity or 0)

    # ----------------------------
    # 5️⃣ @api.constrains
    # ----------------------------
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 0:
                raise ValidationError("Age cannot be negative!")

    # ----------------------------
    # 6️⃣ @api.autovacuum
    # ----------------------------
    @api.autovacuum
    def _autovacuum_cleanup(self):
        print("Autovacuum is running...")

    def action_send_email(self):
        template = self.env.ref('custom_uber.email_template_custom_uber')
        template.send_mail(self.id, force_send=True)


    # ----------------------------
    # 7️⃣ Cron Method for Odoo 18
    # ----------------------------
    @api.model
    def cron_update_totals(self):
        """
        This method will be called by a cron job.
        It recalculates total for all records and logs the result.
        """
        records = self.search([])
        for rec in records:
            old_total = rec.total
            rec.total = (rec.price or 0) * (rec.quantity or 0)
            _logger.info(f"Cron ran for CustomUber {rec.name}: old_total={old_total}, new_total={rec.total}")
        return True
