{
    "name": "WhatsApp Cloud Core",
    "summary": "Base multiempresa para configurar WhatsApp Cloud API y enviar mensajes.",
    "version": "18.0.0.1",
    "author": "Cristhian Medina",
    "license": "LGPL-3",
    "category": "Tools",
    "depends": ["base", "base_setup"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/res_company_views.xml",
        "views/send_wizard_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": False
}