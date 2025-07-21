from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    # Do not redefine company_id field; use constraints and default logic instead

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if 'company_id' in fields and not res.get('company_id'):
            res['company_id'] = self.env.user.company_id.id
        return res

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if not self.company_id:
            return {
                'warning': {
                    'title': _('Advertencia'),
                    'message': _('Debe seleccionar una empresa para el equipo de ventas.'),
                }
            }

    @api.constrains('company_id')
    def _check_company_id(self):
        for record in self:
            if not record.company_id:
                raise ValidationError(_("Debe seleccionar una empresa para el equipo de ventas."))
