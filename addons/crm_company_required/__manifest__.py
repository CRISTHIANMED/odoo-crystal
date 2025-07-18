# crm_company_required/__manifest__.py
{
    'name': 'Todo_CRM_requerir_compañia',
    'version': '1.0',
    'summary': 'Hace que la compañia sea requerida para crear equipos de ventas',
    'category': 'CRM',
    'author': 'Cristhian Medina',
    'depends': ['crm'],
    'data': [
        'views/crm_team_views.xml',
    ],
    'installable': True,
    'application': False,
}
