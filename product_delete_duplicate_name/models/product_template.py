from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def remove_duplicate_products(self):
        products = self.search([])
        for product in products:
            product_name = product.name.upper()
            product_name = product_name.replace('[', '[ ')
            product_name = product_name.replace(']', ' ]')
            words = product_name.split()
            unique_words = []
            [unique_words.append(word) for word in words if word not in unique_words]
            product_name = ' '.join(unique_words)
            product_name = product_name.replace('[ ', '[')
            product_name = product_name.replace(' ]', ']')
            product.name = product_name




