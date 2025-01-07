# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError
import datetime

class CarpoolingAbstractModel(models.AbstractModel):
    _name = 'carpooling.abstract.model'
    _description = 'Carpooling Abstract Model'
    
    @api.onchange('name')
    def _onchange_name(self):
        current_date_year = f"{datetime.datetime.now().year}"
        if self.name:
            if current_date_year not in self.name:
                self.name = f"{self.name} {current_date_year}"

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
    _description = """Carpooling Model"""
    _inherit = ['mail.thread', 'mail.activity.mixin', 'carpooling.abstract.model']
    
    # This sets the default ordering for records: first by 'sequence' in ascending order, then by 'id' in descending order.
    # For tree view
    _order = 'sequence asc, id desc' #
    
    name = fields.Char(string='Name')
    taken_seats = fields.Integer(string='Taken Seats', tracking=True)
    departure_time = fields.Float(string='Departure Time', tracking=True)
    departure_date = fields.Date(string='Departure Date', tracking=True)
    departure_city = fields.Char(string='Departure City', tracking=True)
    destination_city = fields.Char(string='Destination City', tracking=True)
    note = fields.Text(string='Note', tracking=True)
    is_free = fields.Boolean(string='Is Free', tracking=True)
    states = [
        ('new', 'New'),
        ('available', 'Available'),
        ('full', 'Full'),
    ]
    state = fields.Selection(selection=states, string='State', default='new', tracking=True)
    company_currency = fields.Many2one(
        'res.currency', string='Currency', compute='_compute_company_currency', readonly=True
    )
    amount_per_km = fields.Monetary(
        string='Amount per km', currency_field='company_currency', tracking=True
    )
    
    resume = fields.Html(string='Resume', tracking=True)
    image = fields.Binary(string='Image', tracking=True)
    car_id = fields.Many2one('carpooling.car', string='Car', tracking=True)
    tag_ids = fields.Many2many('carpooling.tag', string='Tags', tracking=True)
    km = fields.Float(string='KM', tracking=True)
    cost = fields.Monetary(string='Cost', currency_field='company_currency', compute='_compute_cost', tracking=True)
    brand = fields.Char(string='Brand', related='car_id.brand', tracking=True)
    seats = fields.Integer(string='Seats', related='car_id.seats', tracking=True)
    sequence = fields.Integer(string='Sequence')
    
    @api.onchange('car_id')
    def _onchange_car_id(self):
        """
        Triggered when the 'car_id' field is changed.
        """
        # Search for cars with more than 2 seats and sort by car name
        cars = self.env['carpooling.car'].search([]).filtered(lambda car: car.seats >= 2).sorted(key=lambda car: car.name)
        for car in cars:
            logging.info('Car name: %s', car.name)

    
    # Check if the carpooling trip is free
    # By checking taken_seats and car_id fields
    # Checking car_id is important because car seats must be updated
    @api.onchange('taken_seats', 'car_id')
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
            
    def _run_cron(self):
        for carpool in self.search([]):
            logging.info('Cron job running for carpooling: %s', carpool.name)
            if carpool.departure_time > 12:
                logging.info('Departure time is in the afternoon.')
                carpool.amount_per_km += 25