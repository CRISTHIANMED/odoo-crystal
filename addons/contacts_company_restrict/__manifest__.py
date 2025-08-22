{
    "name": "Contacts Company Restrict",
    "version": "1.0",
    "summary": "Default company_id en Contactos y regla por empresa",
    "author": "Cristhian Medina",
    "license": "LGPL-3",
    "depends": ["base", "contacts"],
    "category": "Contacts",
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False
}