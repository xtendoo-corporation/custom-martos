{
    'name': 'Product Label Printing Wizard Customization',
    'version': '18.0.1.0.0',
    'summary': 'Customizations for the product label printing wizard in Odoo 18',
    'description': """
        This module customizes the product label printing wizard in Odoo 18.
    """,
    'author': 'Abraham Carrasco (Xtendoo)',
    'category': 'Custom',
    'depends': ['base', 'product', 'stock'],
    'data': [
        "report/product_product_templates.xml",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
