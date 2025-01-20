# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError, UserError
import datetime


class CarReport(models.AbstractModel):
    _name = 'report.carpooling.report_template_carpooling_carpooling'
    _description = 'Carpooling Report'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        # Log the docids received
        logging.info(f'[LOG] [CarReport] [_get_report_values] [docids : {docids}]')
        
        # Fetch the carpooling records based on docids
        docs = self.env['carpooling.carpooling'].browse(docids)
        
        # Raise an error if any record does not have a departure date
        if any(not doc.departure_date for doc in docs):
            raise UserError('One or more records do not have a departure date, please fill it')
        
        # Return the report values
        return {
            'doc_ids': docids,
            'doc_model': 'carpooling.carpooling',
            'docs': docs,
            'data': data
        }