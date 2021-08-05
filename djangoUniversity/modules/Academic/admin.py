#from djangoUniversity.modules.Academic.models import Carrer, Course, Student, identificationNumber
from django.contrib import admin
from modules.Academic.models import *

# Register your models here.

admin.site.register(Carrer)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(identificationNumber)
