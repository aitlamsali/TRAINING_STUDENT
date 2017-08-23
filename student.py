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
        ('allumi','Allumi'),
        ('',''),
         ]

class student_student(models.Model):
    _name = 'student.student'
    _description =  'Student Information'

    name=fields.Char(string='Name', required=True, index=True)
    active =fields.Boolean(string='Active', default=true)
    image=fields.Binary(string='Image')
    uni_no=fields.Char(string='University Number', required=True, copy=false)
    seat_no=fields.Integer(string='Name', required=True, index=True, copy=false, default=  , store= , compute= , readonly= )
    dob=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    age=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    gender=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )


    result_ids=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    hobbies_ids=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    responsible_id=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    email=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    phone=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    fdate=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    ldate=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    degree_id=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    regfees=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    tutfees=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    totfees=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    ref=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    ref_link=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    health_issues=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    health_notes=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )
    template=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )

    state=fields.Char(string='Name', required=True, index=True, copy=True, default=  , store= , compute= , readonly= )



