# __manifest__.py
{
    'name': 'Product Quotation Fetcher',
    'version': '17.0.1',
    'category': 'Inventory/Inventory',
    'summary': 'Obtiene cotizaciones de productos desde Yahoo Finance',
    'description': """
        Este módulo agrega la capacidad de obtener cotizaciones 
        de productos desde Yahoo Finance usando la referencia interna
        como símbolo bursátil.
    """,
    'author': 'Tu Empresa',
    'website': 'https://www.tuempresa.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'stock',
    ],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}