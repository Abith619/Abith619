from odoo import api, fields, models, _

class diet(models.Model):
    _name='set.diet.lines'

class SetDiets(models.Model):
    _name = 'set.diets'

    name = fields.Char('Name', required = True)
    # code = fields.Char('Code')
    diet_line = fields.One2many('set.diet.line','name',string="Diet Advisied")
    diet_line1 = fields.One2many('diet.six','name',string="Diet Advisied")
    diet_line2 = fields.One2many('diet.seven','name',string="Diet Advisied")
    diet_line3 = fields.One2many('diet.eight','name',string="Diet Advisied")
    diet_line4 = fields.One2many('diet.nine','name',string="Diet Advisied")
    diet_line5 = fields.One2many('diet.eleven','name',string="Diet Advisied")
    diet_line6 = fields.One2many('diet.one.lunch','name',string="Diet Advisied")
    diet_line7 = fields.One2many('diet.four','name',string="Diet Advisied")
    diet_line8 = fields.One2many('diet.seven.one','name',string="Diet Advisied")
    diet_line9 = fields.One2many('diet.five','name',string="Diet Advisied")

class DietAssign(models.Model):
    _name='set.diet.line'

    name=fields.Many2one('set.diets')

    wakeup1=fields.Char(string="Morning")
    # wakeup=fields.Selection([('ghee','Ghee'),('butter','Butter'),('coconut','Coconut-Oil')],string="Morning")
    note=fields.Char('Notes')

class diet_six(models.Model):
    _name='diet.six'

    name=fields.Many2one('set.diets')
    juice1=fields.Char(string="Juice",default='Sorraka 150ml')
    quantity=fields.Char(string="Quantity")
    exercise1=fields.Char(string="Exercise")
    # juice=fields.Selection([('sorraka','Sorraka Juice'),('nil','Nil')],string="Juice",default='Sorraka 150ml')
    # exercise=fields.Selection([('walking','Walking'),('plank','Plank'),('namaskar','Surya Namaskar'),('strech','Streches'),('namaz','Namaz'),('exercise','Ground Exercise'),('nil','Nil')],string="Exercise")
    note=fields.Char('Notes')

class diet_seven(models.Model):
    _name='diet.seven'

    name=fields.Many2one('set.diets')
    fruits1=fields.Char(string="Fruits")
    # fruits=fields.Many2many('set.fruits',string="Fruits")
    grams=fields.Char('Quantity',default='100 Grams')
    note=fields.Char('Notes')

class diet_eight(models.Model):
    _name='diet.eight'

    name=fields.Many2one('set.diets')
    medicine=fields.Text(string='Medicine')
    milk=fields.Selection([('milk','Milk'),('nil','Nil')],string="Milk")
    note=fields.Char('Notes',default='Milk 100 Grams')

class Friuts(models.Model):
    _name='set.fruits'

    name=fields.Char('Name')
    
class Diet_nine(models.Model):
    _name='diet.nine'

    name=fields.Many2one('set.diets')
    note=fields.Char('Notes')
    quantity=fields.Char('Quantity')
    breakfast=fields.Selection([('yes','Yes'),('no','N0')],string="Breakfast")
    breakfast_list=fields.Selection([('semiya','Red Semiya'),('Aval','Red Aval'),('boiled veg','Boiled-Veg'),('fruit bowl','Fruit Bowl'),('karani arisi kanji','Karani Arisi Kanji'),('ousadha kanji','Ousadha Kanji'),('sathu maavu','Sathu Maavu')],string="Breakfast List")

class diet_eleven(models.Model):
    _name='diet.eleven'

    name=fields.Many2one('set.diets')
    note=fields.Char(string='Notes', default='No Sugar')
    litres=fields.Char(string='Quantity', default='100 ml')
    drinks=fields.Selection([('butter','Butter-Milk'),('coconut','Coconut-Water'),('Anemia','Anemia Juice')],string="Drinks")
    drinks_list=fields.Selection([('Apple','Apple + Carrot'),('beet','Beetroot + Orange'),('grapes','Black Grapes + PineApple'),('pomogranate','Pomogranate + Milk')],string="Drinks List")

class diet_four(models.Model):
    _name='diet.four'

    name=fields.Many2one('set.diets')
    note=fields.Char('Notes')
    snacks1=fields.Char(string="Snacks")
    # snacks=fields.Selection([('coconut','Coconut-Milk 200 ml'),('sp-coconut','SP-Coconut'),('nil','Nil')],string="Snacks")

class diet_seven_one(models.Model):
    _name='diet.five'

    name=fields.Many2one('set.diets')
    note=fields.Char('Notes')
    exercise=fields.Char(string="Exercise")

class diet_seven_one(models.Model):
    _name='diet.seven.one'

    name=fields.Many2one('set.diets')
    note=fields.Char('Notes')
    snackss=fields.Char(string="Snacks")
    snacks12=fields.Char(string="Afternoon")
    # snacks=fields.Selection([('sabzi','Veg-Sabzi 200 gm'),('salad','Veg-Salad 150 gm'),('veg-salad','Veg-Salad 200 gm + Omelete')],string="Snacks")
    # snacks1=fields.Selection([('egg','Egg'),('phulka','Phulka'),('both','Egg & Phulka'),('nil','Nil')],string="Egg / Phulka")
    snacks2=fields.Selection([('semiya','Red Semiya'),('Aval','Red Aval'),('puttu','Red Puttu')],string="Dinner")

class Diet_One(models.Model):
    _name='diet.one.lunch'

    name=fields.Many2one('set.diets')
    fruit_diet=fields.Many2many('set.fruits',string="Fruit Diet")
    veg_diet=fields.Many2many('set.veg',string="Veg Diet")
    grams=fields.Char('Quantity',default='100 Grams')
    rice=fields.Many2many('set.rice',string="Rice")
    protein_diet=fields.Many2many('set.protein',string="Protein Diet")
    note=fields.Char('Notes')
    
class Friuts(models.Model):
    _name='set.veg'

    name=fields.Char('Name')

class Protein_List(models.Model):
    _name='set.protein'

    name=fields.Char('Name')

class Rice_List(models.Model):
    _name='set.rice'

    name=fields.Char('Name')
