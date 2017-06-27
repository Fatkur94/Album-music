"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from music import urls as music_urls
from blog import urls as blog_urls
from . import views as view
#accesing login django



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^path/$', view.index),
    url(r'^user/$', view.display_good2),
    url(r'^meta/$', view.display_meta),
    url(r'^time/$', view.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', view.hours_ahead),
    url(r'^contact/$', view.contact),
    url(r'^listbook/$', view.display_book),
    url(r'^publisher/$', view.PublisherList.as_view()),
    #dont include $  in /music if not adding url again
    #like /music/list etc
    url(r'^music/', include(music_urls, namespace='music')),
    url(r'', include(blog_urls, namespace='blog')),
    
]
