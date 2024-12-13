from odoo import models, api
from odoo.auto.addons.mrp.models.product import ProductProduct
from odoo.auto.addons.sale.models.product_category import ProductCategory


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # @api.model
    # def remove_duplicate_products(self):
    #     products = self.search([])
    #     product_names = {}
    #     for product in products:
    #         print("Product name: ", product.name)
    #         if product.name in product_names:
    #             product.active = False
    #         else:
    #             product_names[product.name] = product.id

    @api.model
    def remove_duplicate_products(self):
        ProductCategory = self.env['product.category']
        products = self.search(["pos_categ_id", "!=", False])
        for product in products:
            product_categ_name = product.categ_id.name
            if product_categ_name.startswith("Todo / "):
                product_categ_name = product_categ_name.replace("Todo / ", "")

            product_category = ProductCategory.search([('name', '=', product_categ_name)], limit=1)
            if product_category:
                product.categ_id = product_category.id
                print("Product category updated: ", product.name, product_category.name)

