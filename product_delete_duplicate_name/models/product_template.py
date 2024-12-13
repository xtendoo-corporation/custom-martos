from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def remove_duplicate_products(self):
        product_category_obj = self.env['product.category']
        products = self.search([])
        for product in products.filtered(lambda p: p.categ_id):
            product_categ_name = product.categ_id.name
            if product_categ_name.startswith("Todo / "):
                product_categ_name = product_categ_name.replace("Todo / ", "")

            print("Product category: ", product_categ_name)

            product_category = product_category_obj.search([('name', '=', product_categ_name)], limit=1)
            if product_category:
                product.categ_id = product_category.id
                print("Product category updated: ", product.name, product_category.name)
            else:
                print("Product category not found: ", product.name, product_categ_name)

