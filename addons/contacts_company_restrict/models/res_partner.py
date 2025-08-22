# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"

    # Reforzamos el default a nivel de campo (también aplica en importaciones si la columna no existe o va vacía)
    company_id = fields.Many2one(
        'res.company',
        default=lambda self: self.env.user.company_id.id,
        # NO pongas required=True si tienes partners antiguos sin compañía; si todo tu histórico la tiene, puedes activarlo.
        # required=True
    )

    @api.model
    def default_get(self, fields_list):
        """
        Asegura que company_id tome por defecto la empresa activa del usuario,
        incluso si el contexto de la vista no lo pone.
        """
        res = super().default_get(fields_list)
        if "company_id" in fields_list and not res.get("company_id"):
            res["company_id"] = self.env.user.company_id.id
        return res

    @api.model_create_multi
    def create(self, vals_list):
        """
        Si al crear (incluido import desde Excel) no se envía company_id,
        se asigna la empresa activa del usuario que ejecuta el proceso.
        """
        user_company_id = self.env.user.company_id.id
        for vals in vals_list:
            # Si el import trae la columna vacía (None/''), también la cubrimos:
            if not vals.get("company_id"):
                vals["company_id"] = user_company_id
        return super().create(vals_list)

    @api.constrains('company_id')
    def _check_company_id(self):
        """
        Validación para impedir que company_id quede vacío.
        """
        for record in self:
            if not record.company_id:
                raise ValidationError(_("Debe seleccionar una empresa para el contacto."))
