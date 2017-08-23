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

