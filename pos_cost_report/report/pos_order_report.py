
from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"
    # total_cost = fields.Float(
    #     string='Total Cost',
    #     readonly=True,
    # )
    # margin = fields.Float(
    #     string='Margin',
    #     readonly=True,
    # )
    #
    # def _select(self):
    #     print("*"*50)
    #     print(super()._select() + ',l.total_cost AS total_cost')
    #     return super()._select() + ',l.total_cost AS total_cost'

