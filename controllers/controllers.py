# -*- coding: utf-8 -*-
from openerp import http

# class TrainingStudent(http.Controller):
#     @http.route('/training__student/training__student/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training__student/training__student/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('training__student.listing', {
#             'root': '/training__student/training__student',
#             'objects': http.request.env['training__student.training__student'].search([]),
#         })

#     @http.route('/training__student/training__student/objects/<model("training__student.training__student"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training__student.object', {
#             'object': obj
#         })