
from odoo import models, fields


class Car(models.Model):
    """
    Car Model
    This model represents a car that can be used for carpooling.
    Attributes:
        name (Char): The name of the car.
    """
    _name = 'car.car'
    _description = """Represents a car that can be used for carpooling"""

    name = fields.Char(string='Name')
    carpooling_ids = fields.One2many('carpooling.carpooling', 'car_id', string='Carpooling Trips')