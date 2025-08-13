
class Sale_order(Models.model):
    _inherit = 'sale.order'

    m_field = fields.Many2one('res.partner', string='Partner')

class Interview_Order(Models.model):
    _name = "hospital.page"

    name = fields.Char(string="Name",)
    age = fields.Float(string="Age")
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Sex")

    doctor = fields.Many2one("res.partner", string='Doctor')
    patient = fields.Many2one("res.partner", string='Patient')


    age_cat = fields.Selection([("child",'Child'), ("adult", "Adult"), ("senior", "Senior")], string="Age Category")

    @api.onchange('age')
    def on_change(self):
        if self.age < 18:
            self.age_cat = "child"
        elif self.age >18:
            self.age_cat = "adult"

    def post_message(self):
        self.description = "The message is posted"
    def post_record(self):
        vals = {
            'name': self.name,
            'age': self.age,
            'doctor': self.doctor
        }
        orm_create = self.env['sale.order'].create(vals)

        print()
    def get_record(self):
        sale_order = self.env["sale.order"].search()

        #customer = sale_order.name

        list = {}
        for i in (sale_order):
            list = {
                'name': i.name,
                'doctor': i.doctor
            }
