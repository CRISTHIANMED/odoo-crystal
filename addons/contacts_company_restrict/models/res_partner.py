# -*- coding: utf-8 -*-
from odoo import api, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def default_get(self, fields_list):
        """
        Asegura que company_id tome por defecto la empresa activa del usuario.
        Funciona aunque el contexto de la vista no lo ponga.
        """
        res = super().default_get(fields_list)
        if "company_id" in fields_list and not res.get("company_id"):
            res["company_id"] = self.env.user.company_id.id
        return res

    @api.model_create_multi
    def create(self, vals_list):
        """
        Si al crear no se envía company_id, se asigna la empresa activa del usuario.
        """
        user_company_id = self.env.user.company_id.id
        for vals in vals_list:
            vals.setdefault("company_id", user_company_id)
        return super().create(vals_list)
    
    @api.constrains('company_id')
    def _check_company_id(self):
        """
        Validación para impedir que company_id quede vacío.
        """
        for record in self:
            if not record.company_id:
                # Mensaje claro y traducible
                raise ValidationError(_("Debe seleccionar una empresa para el contacto."))

