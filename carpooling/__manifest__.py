# -*- coding: utf-8 -*-

{
    'name': 'Carpooling Apps',
    'version': '1.0',
    'author': 'Alain Nambii',
    'description': 
    """
        Helps you to find a carpooling partner
    """,
    'depends': ['base'],
    'category': 'Custom Tools',
    'license': 'LGPL-3',
    'data': [
        'views/carpooling_views.xml',
        'views/carpooling_menus.xml',
        'wizard/carpooling_wizard_views.xml',
        'security/ir.model.access.csv',
    ]
}