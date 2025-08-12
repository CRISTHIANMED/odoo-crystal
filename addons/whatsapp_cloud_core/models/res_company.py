from odoo import fields, models, _
from odoo.exceptions import UserError

class ResCompany(models.Model):
    _inherit = "res.company"

    wa_phone_number_id = fields.Char("WA Phone Number ID", help="ID del número en WhatsApp Cloud.")
    wa_access_token    = fields.Char("WA Access Token", help="Token de Meta.", groups="base.group_system")
    wa_test_number     = fields.Char("Número de prueba (E.164)", help="Ej: 57XXXXXXXXXX")

    def _wa_check(self):
        for c in self:
            if not c.wa_phone_number_id or not c.wa_access_token:
                raise UserError(_("Configura 'WA Phone Number ID' y 'WA Access Token' en la empresa '%s'.") % c.name)

    def wa_send_text(self, to_number: str, message: str):
        self.ensure_one()
        self._wa_check()
        client = self.env["wa.client"]
        return client.send_text(
            phone_number_id=self.wa_phone_number_id,
            access_token=self.wa_access_token,
            to_number=to_number,
            message=message,
        )

    def action_wa_test_send(self):
        for c in self:
            if not c.wa_test_number:
                raise UserError(_("Configura 'Número de prueba' en la empresa '%s'.") % c.name)
            c.wa_send_text(c.wa_test_number, "Mensaje de prueba desde Odoo ✅")
        return True
