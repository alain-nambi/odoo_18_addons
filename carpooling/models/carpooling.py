# -*- coding: utf-8 -*-

from odoo import models, fields

class Carpooling(models.Model):
    """
    Carpooling Model
    This model helps users to find a carpooling partner by providing details about the carpooling trip.
    Attributes:
        name (Char): The name of the carpooling trip.
        taken_seats (Integer): The number of seats that have been taken.
        departure_time (Float): The time of departure for the carpooling trip.
        departure_date (Date): The date of departure for the carpooling trip.
        note (Text): Additional notes or information about the carpooling trip.
        is_free (Boolean): Indicates whether the carpooling trip is free of charge.
        state (Selection): The current state of the carpooling trip, with possible values:
            - 'new': The trip is newly created.
            - 'available': The trip is available for booking.
            - 'full': The trip is fully booked.
    """
    _name = 'carpooling.carpooling'
    _description = """Helps you to find a carpooling partner"""
    
    name = fields.Char(string='Name')
    taken_seats = fields.Integer(string='Taken Seats')
    departure_time = fields.Float(string='Departure Time')
    departure_date = fields.Date(string='Departure Date')
    note = fields.Text(string='Note')
    is_free = fields.Boolean(string='Is Free')
    states = [
        ('new', 'New'),
        ('available', 'Available'),
        ('full', 'Full'),
    ]
    state = fields.Selection(selection=states, string='State', default='new')
    