from odoo import api, fields, models

class Prescribediet(models.Model):
    _name = 'prescribe.diet'

    name = fields.Many2one('set.diets', string="diets",required = True)
    pre_diet_line = fields.One2many('prescribe.diet.line','name',string="Diet Advisied")
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name")
    dates=fields.Date(string='Date',default=fields.Datetime.now(),readonly=True)

    diet_line = fields.One2many('assign.diet.lines','names',string="Diet Advisied")
    diet_line1 = fields.One2many('assign.diet.six','name',string="Diet Advisied")
    diet_line2 = fields.One2many('assign.diet.seven','name',string="Diet Advisied")
    diet_line3 = fields.One2many('assign.diet.eight','name',string="Diet Advisied")
    diet_line4 = fields.One2many('assign.diet.nine','name',string="Diet Advisied")
    diet_line5 = fields.One2many('assign.diet.eleven','name',string="Diet Advisied")
    diet_line6 = fields.One2many('assign.diet.one.lunch','name',string="Diet Advisied")
    diet_line7 = fields.One2many('assign.diet.four','name',string="Diet Advisied")
    diet_line8 = fields.One2many('assign.diet.seven.one','name',string="Diet Advisied")
    diet_line9 = fields.One2many('assign.diet.five','name',string="Diet Advisied")

    @api.onchange('name')
    def onchange_task(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line:
                val={
                    'wakeup1': line.wakeup1,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line1:
                val={
                    'juice1': line.juice1,
                    'quantity':line.quantity,
                    'exercise1':line.exercise1,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line1=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line2:
                val={
                    'fruits1': line.fruits1,
                    'grams':line.grams,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line2=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line3:
                val={
                    'medicine': line.medicine,
                    'milk':line.milk,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line3=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line4:
                val={
                    'breakfast_list': line.breakfast_list,
                    'breakfast':line.breakfast,
                    'quantity':line.quantity,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line4=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line5:
                val={
                    'drinks_list': line.drinks_list,
                    'drinks':line.drinks,
                    'litres':line.litres,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line5=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line6:
                val={
                    'fruit_diet': line.fruit_diet,
                    'veg_diet':line.veg_diet,
                    'protein_diet':line.protein_diet,
                    'grams':line.grams,
                    'rice':line.rice,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line6=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line7:
                val={
                    'snacks1': line.snacks1,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line7=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line8:
                val={
                    'snacks12': line.snacks12,
                    'snackss':line.snackss,
                    'snacks2':line.snacks2,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line8=lines
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line9:
                val={
                    'exercise': line.exercise,
                    'note':line.note,
                }
                lines.append((0,0,val))
            rec.diet_line9=lines


class PrescribeDietAssign(models.Model):
    _name='prescribe.diet.line'


    name=fields.Many2one('prescribe.diet')
    start_time = fields.Float(string="Time")
    meridiem = fields.Selection([('am',"Am"),('pm',"Pm")],string="Am/Pm")
    diet = fields.Char(string="Diet Advised")

class DietAssign(models.Model):
    _name='assign.diet.lines'

    names=fields.Many2one('prescribe.diet')

    wakeup1=fields.Char(string="Morning")
    # wakeup=fields.Selection([('ghee','Ghee'),('butter','Butter'),('coconut','Coconut-Oil')],string="Morning")
    note=fields.Char('Notes')

class diet_six(models.Model):
    _name='assign.diet.six'

    name=fields.Many2one('prescribe.diet')
    juice1=fields.Char(string="Juice",default='Sorraka 150ml')
    quantity=fields.Char(string="Quantity")
    exercise1=fields.Char(string="Exercise")
    # juice=fields.Selection([('sorraka','Sorraka Juice'),('nil','Nil')],string="Juice",default='Sorraka 150ml')
    # exercise=fields.Selection([('walking','Walking'),('plank','Plank'),('namaskar','Surya Namaskar'),('strech','Streches'),('namaz','Namaz'),('exercise','Ground Exercise'),('nil','Nil')],string="Exercise")
    note=fields.Char('Notes')

class diet_seven(models.Model):
    _name='assign.diet.seven'

    name=fields.Many2one('prescribe.diet')
    fruits1=fields.Char(string="Fruits")
    grams=fields.Char('Quantity',default='100 Grams')
    note=fields.Char('Notes')

class diet_eight(models.Model):
    _name='assign.diet.eight'

    name=fields.Many2one('prescribe.diet')
    medicine=fields.Text(string='Medicine')
    milk=fields.Selection([('milk','Milk'),('nil','Nil')],string="Milk")
    note=fields.Char('Notes',default='Milk 100 Grams')


    
class Diet_nine(models.Model):
    _name='assign.diet.nine'

    name=fields.Many2one('prescribe.diet')
    note=fields.Char('Notes')
    quantity=fields.Char('Quantity')
    breakfast=fields.Selection([('yes','Yes'),('no','N0')],string="Breakfast")
    breakfast_list=fields.Selection([('semiya','Red Semiya'),('Aval','Red Aval'),('boiled veg','Boiled-Veg'),('fruit bowl','Fruit Bowl'),('karani arisi kanji','Karani Arisi Kanji'),('ousadha kanji','Ousadha Kanji'),('sathu maavu','Sathu Maavu')],string="Breakfast List")

class diet_eleven(models.Model):
    _name='assign.diet.eleven'

    name=fields.Many2one('prescribe.diet')
    note=fields.Char(string='Notes', default='No Sugar')
    litres=fields.Char(string='Quantity', default='100 ml')
    drinks=fields.Selection([('butter','Butter-Milk'),('coconut','Coconut-Water'),('Anemia','Anemia Juice')],string="Drinks")
    drinks_list=fields.Selection([('Apple','Apple + Carrot'),('beet','Beetroot + Orange'),('grapes','Black Grapes + PineApple'),('pomogranate','Pomogranate + Milk')],string="Drinks List")

class diet_four(models.Model):
    _name='assign.diet.four'

    name=fields.Many2one('prescribe.diet')
    note=fields.Char('Notes')
    snacks1=fields.Char(string="Snacks")
    # snacks=fields.Selection([('coconut','Coconut-Milk 200 ml'),('sp-coconut','SP-Coconut'),('nil','Nil')],string="Snacks")

class diet_seven_one(models.Model):
    _name='assign.diet.five'

    name=fields.Many2one('prescribe.diet')
    note=fields.Char('Notes')
    exercise=fields.Char(string="Exercise")

class diet_seven_one(models.Model):
    _name='assign.diet.seven.one'

    name=fields.Many2one('prescribe.diet')
    note=fields.Char('Notes')
    snackss=fields.Char(string="Snacks")
    snacks12=fields.Char(string="Afternoon")
    # snacks=fields.Selection([('sabzi','Veg-Sabzi 200 gm'),('salad','Veg-Salad 150 gm'),('veg-salad','Veg-Salad 200 gm + Omelete')],string="Snacks")
    # snacks1=fields.Selection([('egg','Egg'),('phulka','Phulka'),('both','Egg & Phulka'),('nil','Nil')],string="Egg / Phulka")
    snacks2=fields.Selection([('semiya','Red Semiya'),('Aval','Red Aval'),('puttu','Red Puttu')],string="Dinner")

class Diet_One(models.Model):
    _name='assign.diet.one.lunch'

    name=fields.Many2one('prescribe.diet')
    fruit_diet=fields.Many2many('set.fruits',string="Fruit Diet")
    veg_diet=fields.Many2many('set.veg',string="Veg Diet")
    grams=fields.Char('Quantity',default='100 Grams')
    rice=fields.Many2many('set.rice',string="Rice")
    protein_diet=fields.Many2many('set.protein',string="Protein Diet")
    note=fields.Char('Notes')
    

