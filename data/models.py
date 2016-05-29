#-*- coding: utf-8 -*-
from django.db import models

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

class Employees(models.Model):
	first_name = models.CharField(max_length=100, verbose_name="фамилия") 
	last_name = models.CharField(max_length=100, verbose_name="имя")
	mid_name = models.CharField(max_length=100, verbose_name="отчество")
	date_enter = models.DateField(blank=True, null=True, verbose_name="дата_принятия")
	date_dismis = models.DateField(blank=True, null=True, verbose_name="дата_увольнения")
	num_pass = models.CharField(max_length=8, verbose_name="№паспорта")
	inn = models.CharField(max_length=10, verbose_name="ИНН")
	phone = models.CharField(max_length=12, verbose_name="телефон")

	class Meta(object):
		verbose_name_plural = 'Работники'
		verbose_name = 'Работник'