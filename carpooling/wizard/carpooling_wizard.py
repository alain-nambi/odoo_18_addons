from odoo import models, fields
from odoo.exceptions import ValidationError


class CarpoolingWizard(models.TransientModel):
    _name = 'carpooling.wizard'
    _description = 'Carpooling Wizard'
    
    departure = fields.Char(string='Departure')
    destination = fields.Char(string='Destination City')
    departure_date = fields.Date(string='Departure Date')
    
    def action_search_trip(self):
        """
        Search for a carpooling trip that matches the user's criteria.
        """
        carpool = self.env['carpooling.carpooling'].search([
            ('departure_city', '=', self.departure),
            ('destination_city', '=', self.destination),
            ('departure_date', '=', self.departure_date),
        ])
        
        if carpool:
            raise ValidationError(f'Carpooling trip found! : {carpool.id}')
        else:
            raise ValidationError('No carpooling trip found!')
    