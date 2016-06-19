#-*- coding: utf-8 -*-
from django.contrib import admin
#from django.contrib.admin import SimpleListFilter
# Register your models here.
from .models import Countries, Continents, Citizenship, Suppliers
from .models import Workshops, Plots, Storeges, Brigades, Equipments
from .models import Items, Childrens, Status, Positions, Orders, Employees

# Также добавить остальные таблицы
class CountriesAdmin(admin.ModelAdmin):
	list_display = ('id','c_name', 'currency')
	list_filter = ('id','c_name', 'currency',)
	search_fields = ['id','c_name', 'currency',]
#	def suit_cell_attributes(self, obj, column):
#		if column == 'страна' or 'Страна':
			#return {'class': 'text-center'}
#			return {'countries-c_name': 'text-center'}
#		elif column == 'валюта' or 'Валюта':
#			return {'class': 'text-center'}

class ContinentsAdmin(admin.ModelAdmin):
	list_display = ('id','cn_name')
	list_filter = ('id','cn_name',)
	search_fields = ['id','cn_name',]

class CitizenshipAdmin(admin.ModelAdmin):
	list_display = ['id', 'id_country', 'id_continent', 'date_obtain', 'autochthon']
	list_filter = ('id', 'id_country', 'id_continent', 'date_obtain', 'autochthon',)
	search_fields = ['id', 'date_obtain', 'autochthon',]
#'id_country', 'id_continent',

class SuppliersAdmin(admin.ModelAdmin):
	list_display = ['id', 's_name', 'id_country', 'city_name', 'phone', 'address']
	list_filter = ('id', 's_name', 'id_country', 'city_name', 'phone', 'address',)
	search_fields = ['id', 's_name', 'city_name', 'phone', 'address',]
#'id_country'

class WorkshopsAdmin(admin.ModelAdmin):
	list_display = ['id', 'w_name']
	list_filter = ('id', 'w_name',)
	search_fields = ['id', 'w_name',]

class PlotsAdmin(admin.ModelAdmin):
	list_display = ['id', 'p_name', 'id_stor']
	list_filter = ('id', 'p_name', 'id_stor',)
	search_fields = ['id', 'p_name',]
#'id_stor'
class StoregesAdmin(admin.ModelAdmin):
	list_display = ['id', 's_name', 'id_stor']
	list_filter = ('id', 's_name', 'id_stor',)
	search_fields = ['id', 's_name',]

class BrigadesAdmin(admin.ModelAdmin):
	list_display = ['id', 'br_name', 'id_plot']
	list_filter = ('id', 'br_name', 'id_plot',)
	search_fields = ['id', 'br_name',]
#'id_plot'

class EquipmentsAdmin(admin.ModelAdmin):
	list_display = ['id', 'eq_name', 'id_plot', 'cost']
	list_filter = ('id', 'eq_name', 'id_plot', 'cost',)
	search_fields = ['id', 'eq_name', 'cost',]
#'id_plot'
class ItemsAdmin(admin.ModelAdmin):
	list_display = ['id', 'id_supp', 'id_plot', 'it_name', 'price', 'for_count']
	list_filter = ('id', 'id_supp', 'id_plot', 'it_name', 'price', 'for_count',)
	search_fields = ['id', 'it_name', 'for_count',]
#'id_supp', 'id_plot','price'
class ChildrensAdmin(admin.ModelAdmin):
	list_display = ['id', 'ch_count', 'desc']
	list_filter = ('id', 'ch_count', 'desc',)
	search_fields = ['id', 'ch_count', 'desc',]

class StatusAdmin(admin.ModelAdmin):
	list_display = ['id', 'status', 'ID_child']
	list_filter = ('id', 'status', 'ID_child',)
	search_fields = ['id', 'status',]
#'ID_child',
class PositionsAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'rank', 'salary']
	list_filter = ('id', 'name', 'rank', 'salary',)
	search_fields = ['id', 'name', 'rank',]
#'salary',
class OrdersAdmin(admin.ModelAdmin):
	list_display = ['id', 'ord_name']
	list_filter = ('id', 'ord_name',)
	search_fields = ['id', 'ord_name',]

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','mid_name', 'ID_status',
    	'ID_ctsh','passport', 'inn', 'ID_posit','phone', 'ID_plot',
    	'date_bday','date_enter','date_dismis','ID_order')
    list_filter = ('id','first_name','last_name','mid_name', 'ID_status',
    	'ID_ctsh','passport', 'inn', 'ID_posit','phone', 'ID_plot',
    	'date_bday','date_enter','date_dismis','ID_order', )
    search_fields = ['id','first_name','last_name','mid_name','passport',
    	'inn', 'phone','date_bday','date_enter','date_dismis',]
#'ID_status','ID_ctsh','ID_posit', 'ID_plot','ID_order'
#Employees, Countries, Continents, Citizenship, Suppliers, 
#	Workshops, Plots, Storeges, Brigades, Equipments, Items, Childrens, 
#	Status, Positions, Orders

# Регистрация таблиц в админ. панель:
#admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Continents, ContinentsAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(Workshops, WorkshopsAdmin)
admin.site.register(Plots, PlotsAdmin)
admin.site.register(Storeges, StoregesAdmin)
admin.site.register(Brigades, BrigadesAdmin)
admin.site.register(Equipments, EquipmentsAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Childrens, ChildrensAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Positions, PositionsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Employees, EmployeesAdmin)

