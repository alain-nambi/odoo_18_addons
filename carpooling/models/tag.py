from odoo import models, fields


class Tag(models.Model):
    """
    Tag Model
    This model represents a tag that can be used to categorize carpooling trips.
    Attributes:
        name (Char): The name of the tag.
    """
    _name = 'carpooling.tag'
    _description = """Represents a tag that can be used to categorize carpooling trips"""

    name = fields.Char(string='Name')
    carpooling_ids = fields.Many2many('carpooling.carpooling', string='Carpooling Trips')