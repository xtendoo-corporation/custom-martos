from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def remove_duplicate_products(self):
        pos_category_obj = self.env['pos.category']
        products = self.search([])
        for product in products.filtered(lambda p: p.categ_id):
            product_categ_name = product.categ_id.name
            if product_categ_name.startswith("Todo / "):
                product_categ_name = product_categ_name.replace("Todo / ", "")

            print("Product category: ", product_categ_name)

            pos_category = pos_category_obj.search([('name', '=', product_categ_name)], limit=1)
            if pos_category:
                product.pos_categ_ids = [(6, 0, [pos_category.id])]
                print("Product category updated: ", product.name, pos_category.name)
            else:
                print("Product category not found: ", product.name, product_categ_name)

