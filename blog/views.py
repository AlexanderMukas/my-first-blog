# -*- coding: utf-8 -*-
from django.shortcuts import render
#08.05.2016 mukas If page don't found
from django.shortcuts import get_object_or_404
#22.05.2016 Добавим пользователя в view.py
from django.contrib import auth

# Добавляем модуль с текущим временем по час.поясу
from django.utils import timezone
# 02.05.2016 - Импортируем модель Post
from .models import Post
# 10.06.2016 Pagination for post_list
from django.core.paginator import Paginator

# 02.05.2016 - Добавляем логику приложения. Вьюшки берут инфо
# с модели, манипулируют, и передают шаблону результат

def post_list(request, page_number=1):
	# paginator
	#all_posts = Post.objects.all()
	all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	current_page = Paginator(all_posts, 4) # данная страница, по 2 поста на стринице
	# Дописали posts. Выборка всех постов и сортировка по дате публикации
	# 08.05.2016 -published_date - если с минусом = order_by desc
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	#22.05.2016 Добавляем имя юзера на страничку
	username = auth.get_user(request).username
	#return render(request, 'blog/post_list.html', {'posts': posts, 'username': username})
	return render(request, 'blog/post_list.html', {'posts': current_page.page(page_number), 'username': username})
# 08.05.2016
def post_detail(request, pk):
	#url = Post.get_absolute_url(Post)
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post' : post})

#21.05.2016 Дописываем 3 раздела.
#"Контакты", "О проекте", "База данных":
def contacts(request):
	# "Контакты" 
	return render(request, 'blog/contacts.html')
# blog/contacts.html пока что нет, нужно его создать, как и URL.

#22.05.2016 раздел "О проекте", about.html
def about(request):
	return render(request, 'blog/about.html')

#def admin-panel(request):
#	return render(request, '')

