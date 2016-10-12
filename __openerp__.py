# -*- coding: utf-8 -*-
##############################################################################
#
#
#    Copyright (C) 2016 Creación y Diseño Ibense, S.L.U.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    $1 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'Personalizaciones visuales odoo',
    'summary': """""",

    'description': """
        Personalizacion de colores odoo
    """,

    'author': "Javier Nadal",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'hilex modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable' : True,
	'application' : True,
	'auto_install' : False,
}