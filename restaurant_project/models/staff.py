from odoo import models, fields


class RestStaff(models.Model):
    _name = 'res.staff'
    _description = 'This model will store the data of our staff'

    _rec_name = 'email'
    _order = 'age desc'

    name = fields.Char(string='Name', size=50)
    age = fields.Integer(string='Age')
    dob = fields.Date(string='DOB')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    #     example of many2one from res.country model
    country_id = fields.Many2one('res.country', string="Country")
    #     example of many2many from res.country model
    country_ids = fields.Many2many('res.country', string="Countries")
    #     Related field
    country_code = fields.Char(string='Country code', related='country_id.code')
    #     One2many field
    staff_line_ids = fields.One2many('res.staff.line', 'connecting_field', string='Staff Line')
    sequence = fields.Integer(string='Seq.')
    status = fields.Selection([('active', 'Active'), ('resigned', 'Resigned')], readonly=True, default='active')

    def new_fun(self):
        print('Executed a function by button')

    def delete_one2many(self):
        for record in self:
            record.staff_line_ids = [(5, 0, 0)]

    def do_resign(self):
        for rec in self:
            rec.status = 'resigned'


class RestStaffLine(models.Model):
    _name = 'res.staff.line'
    _description = 'For maintaining staff details'

    connecting_field = fields.Many2one('res.staff', string='Staff ID')
    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.product', string='Product')
    sequence = fields.Integer(string='Seq.')
