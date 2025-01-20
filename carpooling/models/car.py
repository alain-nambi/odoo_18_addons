
from odoo import models, fields


class Car(models.Model):
    """
    Car Model
    This model represents a car that can be used for carpooling.
    Attributes:
        name (Char): The name of the car.
    """
    _name = 'carpooling.car'
    _description = """Represents a car that can be used for carpooling"""

    name = fields.Char(string='Name')
    carpooling_ids = fields.One2many('carpooling.carpooling', 'car_id', string='Carpooling Trips')
    brand = fields.Char(string='Brand')
    seats = fields.Integer(string='Seats')
    

class Bike(models.Model):
    """
    Bike Model
    """
    _name = 'carpooling.bike'
    _description = """Represents a bike that can be used for carpooling"""
    _inherit = ['carpooling.car']
    
    bike_type = fields.Selection([
        ('sport', 'Sport'),
        ('city', 'City'),
        ('offroad', 'Offroad')
    ])