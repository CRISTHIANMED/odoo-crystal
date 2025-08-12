from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SendWhatsAppWizard(models.TransientModel):
    _name = "send.whatsapp.wizard"
    _description = "Enviar WhatsApp"

    company_id = fields.Many2one(
        "res.company",
        string="Empresa",
        default=lambda self: self.env.company,
        required=True,
        help="Empresa cuyos credenciales (Phone Number ID + Access Token) se usarán."
    )
    to_number = fields.Char(
        string="Enviar a (E.164)",
        required=True,
        help="Ej: 57XXXXXXXXXX (solo dígitos, incluye indicativo de país)."
    )
    message = fields.Text(
        string="Mensaje",
        required=True,
        default="Hola desde Odoo 👋"
    )

    @api.constrains("to_number")
    def _check_to_number(self):
        for w in self:
            if not (w.to_number and w.to_number.isdigit()):
                raise UserError(_("El número debe ser solo dígitos (formato E.164)."))

    def action_send(self):
        self.ensure_one()
        self.company_id.wa_send_text(self.to_number, self.message)
        return {"type": "ir.actions.act_window_close"}
