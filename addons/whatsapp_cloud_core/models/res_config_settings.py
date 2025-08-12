# Ajustes (Settings) multiempresa con fields related → editas por compañía activa.
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    wa_phone_number_id = fields.Char(related="company_id.wa_phone_number_id", readonly=False)
    wa_access_token    = fields.Char(related="company_id.wa_access_token", readonly=False)
    wa_test_number     = fields.Char(related="company_id.wa_test_number", readonly=False)

    def action_whatsapp_test_from_settings(self):
        self.ensure_one()
        (self.company_id or self.env.company).action_wa_test_send()
        return True
