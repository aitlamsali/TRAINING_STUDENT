from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning
from datetime import datetime

STATE = [('draft','Draft'),
        ('med_interview','Medical Interview'),
        ('acad_interview','Academic Interview'),
        ('first_register','First Year Registred'),
        ('second_register', 'Second Year Registred'),
        ('third_register', 'Third Year Registred'),
        ('fourth_register', 'Fourth Year Registred'),
        ('dismiss', 'Dismissed'),
        ('allumi','Allumi'),
         ]

class student_student(models.Model):
    _name = 'student.student'
    _description =  'Student Information'

    name=fields.Char(string='Name', required=True, index=True)
    active =fields.Boolean(string='Active', default=True)
    image=fields.Binary(string='Image')
    uni_no=fields.Char(string='University Number', required=True, copy=False)
    seat_no=fields.Char(string='Seat No', copy=False)
    dob=fields.Date(string='Date of Birth', required=True)
    age=fields.Integer(string='Age')
    gender=fields.Selection([('male','Male'),('female','Female')], 'Gender', default='male')

    result_ids=fields.One2Many('schoolresults.detail', 'student_id', 'School Results')
    hobbies_ids=fields.Many2Many('hobbies.detail', 'student_hobbies_rel', 'student_id', 'hobbie_id', 'Hobbies Information')

    responsible_id=fields.Many2One('res.partner', 'Responsible Person / NOK')
    email=fields.Char(related='responsible_id.email')
    phone=fields.Char(related='responsible_id.phone')

    fdate=fields.Date(string='First Registration Date')
    ldate=fields.Date(string='Last Registration Date')

    degree_id=fields.Many2One('degree.detail', 'Degree to Register For')

    regfees=fields.Float(string='Registration Fees', default='0.0')
    tutfees=fields.Float(string='Tuition Fees', default='0.0')
    totfees=fields.Float(string='Total fees', store=True, readonly=True, compute='_get_total_fees')

    ref=fields.reference(selection=[('res.partner','Partner'),('res.user','User'),('student.student', 'Student')], string='Reference')

    ref_link=fields.Char(string='External Link')

    health_issues=fields.Selection([('yes','Yes'),('no','No')],string='Health Issues', default='no')
    health_notes=fields.Text(string='Health Notes', copy=False )
    template=fields.Html(string='Template')

    state=fields.Selection(STATE, 'Status', readony=True, default='draft')



