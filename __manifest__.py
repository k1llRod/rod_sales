# -*- coding: utf-8 -*-
{
    'name': "rod_sales",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_margin','report_py3o'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        # 'views/sale_order.xml',
        # 'views/stock_move_line.xml',
        'views/sale_order_line.xml',
        'views/commission.xml',
        'views/res_partner.xml',
        'views/res_users.xml',
        'report/report_sale.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

