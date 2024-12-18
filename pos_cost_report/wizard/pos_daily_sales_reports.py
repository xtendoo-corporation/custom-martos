# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class PosDailyReportPerEmployee(models.TransientModel):
    _inherit = 'pos.daily.sales.reports.wizard'

    # add_report_cost = fields.Boolean(string='Add a report cost column', default=True)
    #
    # def _get_report_data(self, pos_session_id):
    #     pos_session = self.env['pos.session'].browse(pos_session_id)
    #     return {'date_start': False, 'date_stop': False, 'config_ids': pos_session.config_id.ids, 'session_ids': pos_session.ids}
    #
    # def get_single_report_print_action(self, pos_session_id):
    #     data = self._get_report_data(pos_session_id)
    #     return self.env.ref('point_of_sale.sale_details_report').report_action([], data=data)

    # def get_multi_report_print_action(self, pos_session_id, employee_ids):
    #     data = self._get_report_data(pos_session_id)
    #     data['employee_ids'] = employee_ids
    #     return self.env.ref('pos_hr.multi_employee_sales_report_action').report_action([], data=data)


