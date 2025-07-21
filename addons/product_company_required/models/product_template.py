from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    company_id = fields.Many2one(
        'res.company',
        string='Empresa',
        default=lambda self: self.env.company,
        required=True
    )

    @api.constrains('company_id')
    def _check_company_id(self):
        for record in self:
            if not record.company_id:
                raise ValidationError("¡Debe seleccionar una Empresa para crear el producto!")

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if not self.company_id:
            return {
                'warning': {
                    'title': _('Advertencia'),
                    'message': _('Debe seleccionar una empresa para el producto.'),
                }
            }
