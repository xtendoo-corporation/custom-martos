from odoo import models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def remove_duplicate_products(self):
        products = self.search([])
        product_names = {}
        for product in products:
            print("Product name: ", product.name)
            if product.name in product_names:
                product.active = False
            else:
                product_names[product.name] = product.id
