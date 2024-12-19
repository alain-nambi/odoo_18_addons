# -*- coding: utf-8 -*-

from odoo import models, fields

class Carpooling(models.Model):
    _name = 'carpooling.carpooling'
    _description = """Helps you to find a carpooling partner"""
    
    name = fields.Char(string='Name')
    taken_seats = fields.Integer(string='Taken Seats')
    