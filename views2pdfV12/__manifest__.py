# coding: utf-8
# Odoo 12

{
    'name': 'views2pdf',
    'version': '12',
    'author': 'captivea-jpa',
    'description': """
Generate PDF from Views
=========================

This module will allow you to generate a pdf report from any views (FORM, TREE, KANBAN, PIVOT, GRAPH, Galendar) in Odoo v12.
Based on https://www.odoo.com/apps/modules/10.0/views2pdf/ by Abderrahmen Khalledi.

    """,
    'license': 'AGPL-3',
    'depends': ['base', 'web'],
    'data': ['views/assets.xml'],
    'qweb': ['static/src/xml/view.xml'],
    'application': False,
    'auto_install': False,
    'installable': True,
}
