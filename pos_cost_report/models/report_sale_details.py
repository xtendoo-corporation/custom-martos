from dataclasses import fields

from odoo import models, api, fields

class ReportSaleDetailsCustom(models.AbstractModel):
    _inherit = 'report.point_of_sale.report_saledetails'

    sum_total_cost = fields.Float(
        string='Total Cost',
        readonly=True
    )
    sum_margin = fields.Float(
        string='Margin',
        readonly=True
    )


    @api.model
    def get_sale_details(self, date_start=False, date_stop=False, config_ids=False, session_ids=False, **kwargs):
        # Call the super method to get the original sale details
        sale_details = super(ReportSaleDetailsCustom, self).get_sale_details(date_start, date_stop, config_ids, session_ids, **kwargs)
        domain = self._get_domain(date_start, date_stop, config_ids, session_ids, **kwargs)
        orders = self.env['pos.order'].search(domain)

        sum_total_cost = 0.0
        sum_margin = 0.0
        for order in orders:
            for order_line in order.lines:
                sum_total_cost += order_line.total_cost
                sum_margin += order_line.margin

        sale_details['sum_total_cost'] = sum_total_cost
        sale_details['sum_margin'] = sum_margin
        return sale_details
