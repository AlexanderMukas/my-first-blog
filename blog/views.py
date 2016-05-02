# -*- coding: utf-8 -*-
from django.shortcuts import render

# Добавляем модуль с текущим временем по час.поясу
from django.utils import timezone
# 02.05.2016 - Импортируем модель Post
from .models import Post
#

# 02.05.2016 - Добавляем логику приложения. Вьюшки берут инфо
# с модели, манипулируют, и передают шаблону результат

def post_list(request):
	# Дописали posts. Выборка всех постов и сортировка по дате публикации
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	
	return render(request, 'blog/post_list.html', {'posts': posts})