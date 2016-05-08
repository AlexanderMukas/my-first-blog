from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	# 08.05.2016 add post_detail for post_list.html
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

]