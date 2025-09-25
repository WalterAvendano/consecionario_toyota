# este archivo se encarga de definir la metadata y configuración principal de un modulo
{
    'name': 'Consecionario Toyota',
    'version': '17.0.1.0.0',
    'summary': 'Módulo para generar una factura, nota de credito y debito personalizadas con un duplicado para enviar por correo y su respectiva marca de agua ',
    'author': 'Walter Avendano',
    'website': 'https://www.tuweb.com',
    'license': 'AGPL-3',
    'category': 'Accounting/Localizations',
    'depends': [
        'account'
    ],
    'data': [
        'reports/factura_toyota_reporte.xml',                       # creación de opcion de impresión de la factura
        'reports/factura_toyota_template.xml',                      # creación de plantilla de la factura QWEB
        'reports/factura_toyota_reporte_copia.xml',                       # creación de opcion de impresión de la factura
        'reports/factura_toyota_template_copia.xml',                      # creación de plantilla de la factura QWEB
    ],
    'assets': {
        'web.report_assets_common': [
            'consecionario_toyota/static/src/css/style.css',         	# archivo CSS para el estilo 
        ],
    },
    'installable': True,
    'application': False,
}
