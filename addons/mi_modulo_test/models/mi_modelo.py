# -*- coding: utf-8 -*-
# models/mi_modelo.py
# Modelo técnico: mi.modulo.simple
# Campos simples para usar en list/form/search/kanban
from odoo import models, fields

class MiModelo(models.Model):
    _name = "mi.modulo.simple"            # Identificador técnico único
    _description = "Mi Modelo Simple"     # Texto visible para usuarios
    _order = "name"                        # Orden por defecto en list

    # Campos
    name = fields.Char(string="Nombre", required=True)   # Campo principal
    descripcion = fields.Text(string="Descripción")      # Texto libre
    active = fields.Boolean(default=True)                # Convención Odoo para activar/desactivar