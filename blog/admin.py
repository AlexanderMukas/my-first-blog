#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
# 02.05.2015 - Добавляем приложение в админку

from .models import Post

admin.site.register(Post)

