
{
    'name': 'Todo_Producto_requerir_compañia',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Obliga a seleccionar empresa al crear productos',
    'author': 'Cristhian Medina',
    'depends': ['product'],
    'data': [
        'views/product_template_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}