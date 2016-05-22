from django.db import models

# Create your models here.
# 02.05.2016 - Прописываем модель для приложения blog
from django.utils import timezone

SHORT_TEST_LEN = 500

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/post/%i/" % self.id

	def get_short_text(self):
		if len(self.text) > SHORT_TEST_LEN:
			return self.text[:SHORT_TEST_LEN] + '...'
		else:
			return self.text
			
#21.05.2016 Перенести в Data_app
#class Employees(models.Model):
#	first_name = models.CharField(max_length=100) 
#	last_name = models.CharField(max_length=100)
#	mid_name = models.CharField(max_length=100)
#	date_enter = models.DateField(blank=True, null=True)
#	date_dismis = models.DateField(blank=True, null=True)
#	num_pass = models.CharField(max_length=8)
#	inn = models.CharField(max_length=10)
#	phone = models.CharField(max_length=12)
		

		
	