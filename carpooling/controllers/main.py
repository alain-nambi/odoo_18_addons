from odoo.http import Controller, request, route


class CarpoolingController(Controller):
    @route('/carpooling', methods=["GET"], type='http', auth='public', website=True, csrf=False)
    def index(self):
        context = {}
        # Add .sudo() to allow user to access the 'carpooling.carpooling' model
        carpoolings = request.env['carpooling.carpooling'].search([])
        context['carpoolings'] = carpoolings
        
        return request.render('carpooling.carpooling_index', context)