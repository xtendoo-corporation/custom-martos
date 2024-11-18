from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'
    _description = 'Choose the sheet layout to print the labels'

    print_format = fields.Selection(selection_add=[
        ('38x21', '38x21')
    ], string="Format", default='38x21', required=True, ondelete={'38x21': 'cascade'})


    def _prepare_report_data(self):
        if self.custom_quantity <= 0:
            raise UserError(_('You need to set a positive quantity.'))

        # Get layout grid
        if self.print_format == 'dymo':
            xml_id = 'product.report_product_template_label_dymo'
        elif self.print_format == '38x21':
            # xml_id = 'product.report_product_template_label_dymo'
            xml_id = 'product_label_custom.report_product_label_38x21'
        elif 'x' in self.print_format:
            xml_id = 'product.report_product_template_label_%sx%s' % (self.columns, self.rows)
            if 'xprice' not in self.print_format:
                xml_id += '_noprice'
        else:
            xml_id = ''

        active_model = ''
        if self.product_tmpl_ids:
            products = self.product_tmpl_ids.ids
            active_model = 'product.template'
        elif self.product_ids:
            products = self.product_ids.ids
            active_model = 'product.product'
        else:
            raise UserError(_("No product to print, if the product is archived please unarchive it before printing its label."))

        # Build data to pass to the report
        data = {
            'active_model': active_model,
            'quantity_by_product': {p: self.custom_quantity for p in products},
            'layout_wizard': self.id,
            'price_included': 'xprice' in self.print_format,
        }
        return xml_id, data


    def process(self):
        self.ensure_one()
        xml_id, data = self._prepare_report_data()
        if not xml_id:
            raise UserError(_('Unable to find report template for %s format', self.print_format))
        print("XML ID:", xml_id)
        print("Data:", data)
        report_action = self.env.ref(xml_id).report_action(None, data=data, config=False)
        report_action.update({'close_on_report_download': True})
        return report_action
