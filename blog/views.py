# -*- coding: utf-8 -*-
from django.shortcuts import render
#08.05.2016 mukas If page don't found
from django.shortcuts import get_object_or_404


# Добавляем модуль с текущим временем по час.поясу
from django.utils import timezone
# 02.05.2016 - Импортируем модель Post
from .models import Post
#

# 02.05.2016 - Добавляем логику приложения. Вьюшки берут инфо
# с модели, манипулируют, и передают шаблону результат

def post_list(request):
	# Дописали posts. Выборка всех постов и сортировка по дате публикации
	# 08.05.2016 -published_date - если с минусом = order_by desc
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	
	return render(request, 'blog/post_list.html', {'posts': posts})
# 08.05.2016
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post' : post})

