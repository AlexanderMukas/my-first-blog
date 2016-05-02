# -*- coding: utf-8 -*- 
# 02.05.2016 - Конфигурация URL адресов.
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # 02.05.16 Домашняя страничка
    url(r'', include('blog.urls')),
    #
]
