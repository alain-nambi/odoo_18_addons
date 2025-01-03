# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

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
        company_currency (Many2one): The currency used by the company.
        amount_per_km (Monetary): The amount charged per kilometer.
        resume (Html): A detailed description of the carpooling trip.
        image (Binary): An image related to the carpooling trip.
        car_id (Many2one): The car used for the carpooling trip.
        tag_ids (Many2many): Tags associated with the carpooling trip.
        km (Float): The distance of the carpooling trip in kilometers.
        cost (Monetary): The total cost of the carpooling trip.
        brand (Char): The brand of the car used for the carpooling trip.
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
    company_currency = fields.Many2one(
        'res.currency', string='Currency', compute='_compute_company_currency', readonly=True
    )
    amount_per_km = fields.Monetary(
        string='Amount per km', currency_field='company_currency'
    )
    resume = fields.Html(string='Resume')
    image = fields.Binary(string='Image')
    car_id = fields.Many2one('carpooling.car', string='Car')
    tag_ids = fields.Many2many('carpooling.tag', string='Tags')
    km = fields.Float(string='KM')
    cost = fields.Monetary(string='Cost', currency_field='company_currency', compute='_compute_cost')
    brand = fields.Char(string='Brand', related='car_id.brand')
    
    @api.onchange('taken_seats', 'state')
    def _onchange_taken_seats(self):
        """
        Triggered when the 'taken_seats' field is changed.
        Updates the 'state' field based on the number of seats taken.
        """
        for record in self:
            if record.taken_seats == 0:
                record.state = 'new'
            elif record.taken_seats < record.car_id.seats:
                record.state = 'available'
            else:
                record.state = 'full'
                record.is_free = False
    
    @api.constrains('km', 'taken_seats')
    def _check_km_value(self):
        """
        Constraint method to validate the values of 'km' and 'taken_seats' fields.

        This method ensures that:
        1. The 'km' (kilometers) value is not negative.
        2. The 'taken_seats' value does not exceed the number of seats available in the car.

        Raises:
            ValidationError: If 'km' is negative or if 'taken_seats' exceeds the car's available seats.
        """
        for record in self:
            if record.km <= 0:
                raise ValidationError(f'Negative or Zero KM value: {record.km} is not allowed.')
            if record.taken_seats > record.car_id.seats:
                raise ValidationError(f'Taken seats {record.taken_seats} exceed available seats {record.car_id.seats}.')

    @api.depends('km', 'amount_per_km')
    def _compute_cost(self):
        """
        Compute the cost based on the distance in kilometers and the amount per kilometer.
        This method is triggered by changes in the 'km' and 'amount_per_km' fields.
        """
        for record in self:
            record.cost = record.km * record.amount_per_km
                
    @api.depends('company_currency')
    def _compute_company_currency(self):
        """
        Compute the company currency based on the current user's company.
        This method is triggered by changes in the 'company_currency' field.
        """
        for record in self:
            # logging.info("Company currency: %s", self.env.user.company_id.currency_id)
            record.company_currency = self.env.user.company_id.currency_id