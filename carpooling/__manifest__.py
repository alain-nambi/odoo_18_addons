# -*- coding: utf-8 -*-

{
    'name': 'Carpooling Apps',
    'version': '1.0',
    'author': 'Alain Nambii',
    'description': 
    """
        Helps you to find a carpooling partner
    """,
    'depends': ['base', 'mail'],
    'category': 'Custom Tools',
    'license': 'LGPL-3',
    'data': [
        'views/carpooling_views.xml',
        'views/carpooling_menus.xml',
        'views/res_partner_views.xml',
        'views/website_template.xml',
        'wizard/carpooling_wizard_views.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'security/groups.xml',
        'security/access_carpooling_manager.xml',
        'data/ir_cron.xml',
        'report/car_report.xml'
    ]
}