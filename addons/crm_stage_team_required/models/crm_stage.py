from odoo import models, fields, api

class CrmStage(models.Model):
    _inherit = 'crm.stage'

    team_id = fields.Many2one(
        'crm.team',
        string='Sales Team',
        required=True,
        ondelete='restrict'  # <- CAMBIADO AQUÍ
    )

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if 'team_id' in fields and not res.get('team_id'):
            user_team = self.env.user.sale_team_id
            if user_team:
                res['team_id'] = user_team.id
        return res


