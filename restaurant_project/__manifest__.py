# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Restaurant Project',
    'version' : '17.0.0.1',
    'summary': 'Restaurant Management',
    'sequence': -100,
    'description': """

Restaurant Management
    """,
    'category': 'Restaurant',
    'depends': ['base','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/staff_view.xml',
        'views/menu_view.xml'
    ],
    'demo': [
        'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
