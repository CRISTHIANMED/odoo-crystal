# -*- coding: utf-8 -*-
{
    "name": "Mi Módulo Simple",
    "summary": "Acción, menús con icono, vistas list/form/search/kanban para Odoo",
    "description": "Módulo didáctico mínimo para experimentar con ir.actions.act_window e ir.ui.view.",
    "version": "18.0.1.0.0",
    "category": "Tutorial",
    "author": "Cristhian Medina",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/mi_modelo_views.xml"
    ],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": True
}