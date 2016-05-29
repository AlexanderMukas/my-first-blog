#-*- coding: utf-8 -*-
from django.contrib import admin
#from django.contrib.admin import SimpleListFilter
# Register your models here.
from .models import Employees

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','mid_name','date_enter','date_dismis','num_pass','inn','phone')
    list_filter = ('first_name', 'last_name','mid_name','date_enter','date_dismis','num_pass','inn','phone', )
    search_fields = ['first_name', 'last_name','mid_name','date_enter','date_dismis','num_pass','inn','phone', ]
admin.site.register(Employees, EmployeesAdmin)