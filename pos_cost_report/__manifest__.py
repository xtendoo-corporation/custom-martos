# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "POS - Cost Report",
    'category': "Hidden",
    'summary': 'Link module between Point of Sale and HR',
    'depends': [
        'point_of_sale'
    ],
    'data': [
        'wizard/pos_daily_sales_reports.xml',
        'views/pos_session_sales_details.xml',
    ],
    'installable': True,
    'auto_install': True,
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_hr/static/src/**/*',
            'pos_cost_report/static/src/**/*',
        ],
        'web.assets_tests': [
            'pos_hr/static/tests/**/*',
        ],
        'web.assets_backend': [
            'pos_hr/static/src/app/print_report_button/*',
        ],
    },
    'license': 'LGPL-3',
}
