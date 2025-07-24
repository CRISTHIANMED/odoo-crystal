from odoo import models, fields, api

class ChatbotScript(models.Model):
    _inherit = 'chatbot.script'

    company_id = fields.Many2one('res.company', string="Empresa", default=lambda self: self.env.company)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' not in vals:
                vals['company_id'] = self.env.company.id
        return super().create(vals_list)

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if 'title' in fields:
            res['title'] = ''
        return res
