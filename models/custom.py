# -*- coding: utf-8 -*-
from openerp import models, fields

class Personalization(models.Model):
    _name = 'personalization.odoo'
    _description = 'Personalizacion odoo'

    name = fields.Char()
    colors = fields.Selection(string="Colores", selection=[('red', 'rojo'), ('blue', 'azul'), ])