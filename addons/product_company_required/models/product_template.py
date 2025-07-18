from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    company_id = fields.Many2one(
        'res.company',
        string='Empresa',
        required=True,
    )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if 'company_id' in fields_list:
            res['company_id'] = self.env.user.company_id.id
        return res

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if not self.company_id:
            return {
                'warning': {
                    'title': _('Advertencia'),
                    'message': _('Debe seleccionar una empresa para el producto.'),
                }
            }

    @api.constrains('company_id')
    def _check_company_id(self):
        for record in self:
            if not record.company_id:
                raise ValidationError(_("Debe seleccionar una empresa para el producto."))
