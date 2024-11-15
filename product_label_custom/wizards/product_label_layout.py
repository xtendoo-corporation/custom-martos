from odoo import _, api, fields, models

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'
    _description = 'Choose the sheet layout to print the labels'

    print_format = fields.Selection([
        ('dymo', 'Dymo'),
        ('2x7xprice', '2 x 7 with price'),
        ('4x7xprice', '4 x 7 with price'),
        ('4x12', '4 x 12'),
        ('4x12xprice', '4 x 12 with price'),
        ('martos', 'Martos')], string="Format", default='martos', required=True)
