from django.contrib import admin

# Register your models here.
# 02.05.2015 - Добавляем приложение в админку

from .models import Post

# 19.05.2016 add employees
#from .models import Employees

#class EmployeesAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'mid_name', 'date_enter', 'date_dismis', 'num_pass',
#    'inn', 'phone')
#21.05.2016 нужно перенести в Data_app

admin.site.register(Post)

#нужно перенести в Data_app
#admin.site.register(Employees, EmployeesAdmin)