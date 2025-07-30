# crm_stage_team_required/models/crm_stage.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CrmStage(models.Model):
    _inherit = 'crm.stage'

    team_id = fields.Many2one(
        'crm.team',
        string='Equipo de ventas',
        required=True,
        ondelete='restrict',
    )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        team_id = self.env.context.get('default_team_id') or self.env.context.get('team_id')
        if team_id:
            res['team_id'] = team_id
        return res

    @api.model
    def create(self, vals):
        if not vals.get('team_id'):
            raise ValidationError("Debe seleccionar un equipo de ventas para esta etapa.")
        return super().create(vals)

    def action_create_stage(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Crear etapa',
            'res_model': 'crm.stage',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_team_id': self.env.user.sale_team_id.id or False,
            }
        }
