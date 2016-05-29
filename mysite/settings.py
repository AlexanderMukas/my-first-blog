#-*- coding: utf-8 -*-
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#-- 08.05.2016 Django-suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
#--


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8y@^g6!@+r6e(6s^-vn80hbu6fw$#xbs(^8shhxe#3vg(y_gqn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1
# 08.05.2016 add host
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['alexandermukas.pythonanywhere.com']
#ALLOWED_HOSTS = ['*']

# Application definition
# 02.05.2016 - Добавляем созданное приложение blog
INSTALLED_APPS = (
    #08.04.2016 Django-Suit Admin panel install
    'suitlocale',
    'suit',
    'import_export',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 01.05.2016 add blog app
    'blog',
    # 15.05.2016 add comments Disqus
    'disqus',
    # 22.05.2016 add auth/login , auth/logout
    'loginsys',
    # 29.05.2016 data
    'data',
)

# 15.05.2016 add comments Disqus
# api key in https://disqus.com/api/applications/4302772/
DISQUS_API_KEY = 'OurPwnBU0ewhSlYbf8XcUaSv9OPnHfwFJAbRHhPzfRwDyUpkTZ2BDBi9VMK0RiCN'
DISQUS_WEBSITE_SHORTNAME = 'aircraft'
# 


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #22.05.2016 add csrf_token
    'django.middleware.csrf.CsrfViewMiddleware',
    #
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# 02.05.2016 - Добавляем свой временной пояс
#LANGUAGE_CODE = 'en-us'
# 08.05.2016 Добавил, рус
LANGUAGE_CODE = 'ru-ru'
#TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# 02.05.2016 - Добавляем еще строчку. STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 29.05.2016 Django-Suit settings

# Django Suit configuration example
SUIT_CONFIG = {
    #'MENU':(
    # Rename app and set icon
    #    {'app': 'blog', 'label': 'Блог' ,'icon':'icon-leaf', 'models': (
    #        'Post'   #, 'continent', 'kitchensink'
    #    )},
    #),


    # header
    'ADMIN_NAME': 'Aircraft',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    #'MENU_ICONS': {
    #    'Blog': 'icon-leaf',
    #    'Data': 'icon-leaf',
    #    'auth': 'icon-lock',
    #},
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}
