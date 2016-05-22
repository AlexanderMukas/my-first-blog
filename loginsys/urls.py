# -*- coding : utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	# login/logout
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	# 22.05.2016 register
	url(r'^register/$', views.register, name='register'),



# 22.05.2016 из blog/urls.py :
#	url(r'^$', views.post_list, name='post_list'),
	# 08.05.2016 add post_detail for post_list.html
#	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	# 21.05.2016 Для contacts.html
#	url(r'^contacts/$', views.contacts, name='contacts'),
	# 22.05.2016 Для about.html
#	url(r'^about/$', views.about, name='about'),

]