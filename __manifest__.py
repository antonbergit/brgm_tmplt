# -*- coding: utf-8 -*-
{
    'name': "Template Module",
    'summary': """Template Module""",
    'description': """Template Module""",

    'author':       'BRGM',
    'license':      'LGPL-3',
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',

    'installable': True,
    'auto_install': False,
    'application': False,

    'depends': ['base', 'brgm_tmplt'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
