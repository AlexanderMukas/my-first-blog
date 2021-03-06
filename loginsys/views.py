# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
# security
from django.template.context_processors import csrf
# register templates
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
### 22.05.2016 из blog/views.py
# Create your views here.
#08.05.2016 mukas If page don't found
#from django.shortcuts import get_object_or_404
#22.05.2016 Добавим пользователя в view.py
#from django.contrib import auth
# Добавляем модуль с текущим временем по час.поясу
#from django.utils import timezone
# 02.05.2016 - Импортируем модель Post
#from .models import Post
###


def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = " Пользователь не найден"
			return render(request, 'loginsys/login.html', args)
	else:
		return render(request, 'loginsys/login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')

def register(request):
	args = {}
	args.update(csrf(request))
	args['form_reg'] = UserForm()
	#args['form_reg'] = UserCreationForm()
	if request.POST:
		newuser_form = UserForm(request.POST)
		#newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
				password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/')
		else:
			args['form_reg'] = newuser_form
	return render(request, 'loginsys/register.html', args)
