# -*- coding: utf-8 -*-
# from odoo import http


# class Change(http.Controller):
#     @http.route('/change/change', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/change/change/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('change.listing', {
#             'root': '/change/change',
#             'objects': http.request.env['change.change'].search([]),
#         })

#     @http.route('/change/change/objects/<model("change.change"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('change.object', {
#             'object': obj
#         })

