from odoo.http import Controller, request, route


class CarpoolingController(Controller):
    @route('/carpooling', methods=["GET"], type='http', auth='public', website=True, csrf=False)
    def index(self):
        context = {}
        return request.render('carpooling.carpooling_index', context)