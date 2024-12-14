from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def remove_duplicate_products(self):
        pos_category = self.env['pos.category'].search([('name', '=', 'Todo')], limit=1)
        if not pos_category:
            print("POS category not found: Todo")
            return

        products = self.search([])
        for product in products:
            product.pos_categ_ids = [(6, 0, [pos_category.id])]
            print("Product category updated: ", product.name, pos_category.name)

