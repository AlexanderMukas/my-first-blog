from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	# 08.05.2016 add post_detail for post_list.html
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	# 21.05.2016 Для contacts.html
	url(r'^contacts/$', views.contacts, name='contacts'),
	# 22.05.2016 Для about.html
	url(r'^about/$', views.about, name='about'),

]