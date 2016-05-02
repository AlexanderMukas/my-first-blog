# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
# 02.05.2016 - Добавляем логику приложения. Вьюшки берут инфо
# с модели, манипулируют, и передают шаблону результат

def post_list(request):
	return render(request, 'blog/post_list.html', {})