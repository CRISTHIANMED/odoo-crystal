from odoo import models, fields

class ImLivechatReportChannel(models.Model):
    _inherit = 'im_livechat.report.channel'

    company_id = fields.Many2one(
        'res.company',
        related='livechat_channel_id.company_id',
        store=True,
        readonly=True,
        string='Empresa'
    )

class ImLivechatReportOperator(models.Model):
    _inherit = 'im_livechat.report.operator'

    company_id = fields.Many2one(
        'res.company',
        related='livechat_channel_id.company_id',
        store=True,
        readonly=True,
        string='Empresa'
    )
