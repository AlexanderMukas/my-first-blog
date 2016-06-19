#-*- coding: utf-8 -*-
from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
# Create your models here.
#class Работники(models.Model):
#	фамилия = models.CharField(max_length=200)
#	имя = models.CharField(max_length=200)
#	отчество = models.CharField(max_length=200)
#	дата_принятия = DateTimeField(blank=True, null=True)
#	дата_увольнения = DateTimeField(blank=True, null=True)
#	№паспорта = models.CharField(max_length=8)
#	ИНН = models.CharField(max_length=10)
#	телефон = models.CharField(max_length=12)

#class Employees(models.Model):
#	first_name = models.CharField(max_length=100, verbose_name="фамилия") 
#	last_name = models.CharField(max_length=100, verbose_name="имя")
#	mid_name = models.CharField(max_length=100, verbose_name="отчество")
#	date_enter = models.DateField(blank=True, null=True, verbose_name="дата_принятия")
#	date_dismis = models.DateField(blank=True, null=True, verbose_name="дата_увольнения")
#	num_pass = models.CharField(max_length=8, verbose_name="№паспорта")
#	inn = models.CharField(max_length=10, verbose_name="ИНН")
#	phone = models.CharField(max_length=12, verbose_name="телефон")
#	class Meta(object):
#		verbose_name_plural = 'Работники'
#		verbose_name = 'Работник'

# Продождение. 13.06.2016
class Countries(models.Model):
	c_name = models.CharField(max_length=40, verbose_name="страна")
	currency = models.CharField(max_length=30, verbose_name="валюта")
	#def __str__(self):
	#	return self.id
	def __str__(self):
		return "{0} ({1})".format(self.id, self.c_name) 

	class Meta(object):
		verbose_name_plural = 'Страны'
		verbose_name = 'Страна'
# Континенты
class Continents(models.Model):
	cn_name = models.CharField(max_length=40, verbose_name="континент")
	#def __str__(self):
	#	return self.cn_name
	def __str__(self):
		return "{0} ({1})".format(self.id, self.cn_name)

	class Meta(object):
		verbose_name_plural = 'Континенты'
		verbose_name = 'Континент'
# Гражданства
class Citizenship(models.Model):
	id_country = models.ForeignKey('Countries', on_delete=models.CASCADE, 
		verbose_name="ID_страны")
	id_continent = models.ForeignKey('Continents', on_delete=models.CASCADE,
		verbose_name="ID_континента")
	date_obtain = models.DateField(verbose_name="дата_получения")
	autochthon = models.BooleanField(verbose_name="корен.житель")
	def __str__(self):
		return "{0}".format(self.id)
	class Meta(object):
		verbose_name_plural = 'Гражданства'
		verbose_name = 'Гражданство'
# Поставщики
class Suppliers(models.Model):
	s_name = models.CharField(max_length=40, verbose_name="поставщик")
	id_country = models.ForeignKey('Countries', on_delete=models.CASCADE,
		verbose_name="ID_страны")
	city_name  = models.CharField(max_length=40, verbose_name="город")
	phone = models.CharField(max_length=40, verbose_name="телефон")
	address = models.CharField(max_length=100, verbose_name="адрес")
	def __str__(self):
		return "{0} ({1})".format(self.id, self.s_name)

	class Meta(object):
		verbose_name_plural = 'Поставщики'
		verbose_name = 'Поставщик'

# Цех
class Workshops(models.Model):
	w_name = models.CharField(max_length=40, verbose_name="цех")
	def __str__(self):
		return "{0} ({1})".format(self.id, self.w_name)

	class Meta(object):
		verbose_name_plural = 'Цеха'
		verbose_name = 'Цех'
#Участок
class Plots(models.Model):
	p_name = models.CharField(max_length=40, verbose_name="участок")
	id_stor = models.ForeignKey('Workshops', on_delete=models.CASCADE,
		verbose_name="ID_цеха")
	def __str__(self):
		return "{0} ({1})".format(self.id, self.p_name)

	class Meta(object):
		verbose_name_plural = 'Участки'
		verbose_name = 'Участок'
# Склады
class Storeges(models.Model):
	s_name = models.CharField(max_length=40, verbose_name="склад")
	id_stor = models.ForeignKey('Workshops', on_delete=models.CASCADE,
		verbose_name="ID_цеха")
	#phone = models.CharField(max_length=40, verbose_name="телефон")

	class Meta(object):
		verbose_name_plural = 'Склады'
		verbose_name = 'Склад'
#Бригады
class Brigades(models.Model):
	br_name = models.CharField(max_length=40, verbose_name="бригада")
	id_plot = models.ForeignKey('Plots', on_delete=models.CASCADE,
		verbose_name="ID_участка")
	class Meta(object):
		verbose_name_plural = 'Бригады'
		verbose_name = 'Бригада'
# Оборудование
# instal - pip3 django-money
# https://github.com/django-money/django-money
# import moneyed
#from djmoney.models.fields import MoneyField
class Equipments(models.Model):
	eq_name = models.CharField(max_length=40, verbose_name="наименование")
	id_plot = models.ForeignKey('Plots', on_delete=models.CASCADE,
		verbose_name="ID_участка")
	cost = MoneyField(max_digits=10, decimal_places=2,
		default_currency='UAH', verbose_name="цена_оборудования")
	class Meta(object):
		verbose_name_plural = 'Оборудование'
		verbose_name = 'Оборудование'
#Детали
class Items(models.Model):
	id_supp = models.ForeignKey('Suppliers', on_delete=models.CASCADE,
		verbose_name="ID_поставщика")
	id_plot = models.ForeignKey('Plots', on_delete=models.CASCADE,
		verbose_name="ID_участка")
	it_name = models.CharField(max_length=40, verbose_name="наименование")
	price = MoneyField(max_digits=10, decimal_places=2,
		default_currency='UAH', verbose_name="цена")
	for_count = models.CharField(max_length=40, verbose_name="за кол-во")
	class Meta(object):
		verbose_name_plural = 'Детали'
		verbose_name = 'Деталь'
# Дети
class Childrens(models.Model):
	ch_count = models.IntegerField(default=0, verbose_name="кол-во")
	desc = models.TextField(verbose_name="описание")
	def __str__(self):
		return "{0} ({1}:{2})".format(self.id, self.ch_count, self.desc)

	class Meta(object):
		verbose_name_plural = 'Дети'
		verbose_name = 'Ребенок'
# Соц. статус
class Status(models.Model):
	status = models.CharField(max_length=10, verbose_name="соц.статус")
	ID_child = models.ForeignKey('Childrens', on_delete=models.CASCADE,
		verbose_name="ID_кол-ва_детей")
	def __str__(self):
		return "{0} ({1})".format(self.id, self.status)
	class Meta(object):
		verbose_name_plural = 'Соц.статус'
		verbose_name = 'Соц.статус'
# Должность
class Positions(models.Model):
	name = models.CharField(max_length=40, verbose_name="должность")
	rank = models.IntegerField(default=0, verbose_name="категория/разряд")
	salary = MoneyField(max_digits=10, decimal_places=2,
		default_currency='UAH', verbose_name="оплата/мес.")
	def __str__(self):
		return "{0} ({1})".format(self.id, self.name)	
	class Meta(object):
		verbose_name_plural = 'Должности'
		verbose_name = 'Должность'
# Приказы
class Orders(models.Model):
	ord_name = models.CharField(max_length=40, verbose_name="описание")
	def __str__(self):
		#return "{0} ({1})".format(self.id, self.ord_name)
		return "{0}".format(self.id)
	class Meta(object):
		verbose_name_plural = 'Приказы'
		verbose_name = 'Приказ'

class Employees(models.Model):
	first_name = models.CharField(max_length=100, verbose_name="фамилия", null=True) 
	last_name = models.CharField(max_length=100, verbose_name="имя", null=True)
	mid_name = models.CharField(max_length=100, verbose_name="отчество", null=True) 
	ID_status = models.ForeignKey('Status', on_delete=models.CASCADE, default=1,
		verbose_name="ID_соц.статуса")
	ID_ctsh = models.ForeignKey('Citizenship', on_delete=models.CASCADE, default=1,
		verbose_name="ID_гражданства")
	passport = models.CharField(max_length=20, verbose_name="№паспорта", null=True)
	inn = models.CharField(max_length=20, verbose_name="инн")
	ID_posit = models.ForeignKey('Positions', on_delete=models.CASCADE, default=1,
		verbose_name="ID_должности")
	phone = models.CharField(max_length=20, verbose_name="телефон")
	ID_plot = models.ForeignKey('Plots', on_delete=models.CASCADE, default=1,
		verbose_name="ID_участка")
	date_bday = models.DateField(blank=True, verbose_name="дата_рождения", null=True)
	date_enter = models.DateField(blank=True, verbose_name="дата_принятия", null=True)
	date_dismis = models.DateField(blank=True, null=True, verbose_name="дата_увольнения")
	ID_order = models.ForeignKey('Orders', on_delete=models.CASCADE, default=1,
		verbose_name="ID_приказа")
	class Meta(object):
		verbose_name_plural = 'Работники'
		verbose_name = 'Работник'

#Suppliers, Workshops, Plots, Storeges, Brigades, Equipments, Items, Childrens, 
#Status, Positions, Orders    		


		