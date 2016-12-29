"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#coding=utf-8

from django.conf.urls import url
from django.contrib import admin
from littleweb import views
from littleweb import search


urlpatterns = [
    url(r'^$', views.index),
    url(r'index/$', views.index, name="index"),
    url(r'^search_form/$', search.search_form, name="search_form"),
    url(r'^search_post/$', search.search_post, name="search_post"),
    url(r'^search/$', search.search, name="search"),
    url(r'^add/(\d+)/(\d+)/$', views.add, name="add"),
    url(r'^admin/', admin.site.urls),
]
