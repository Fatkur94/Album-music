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
from music import urls as music_urls
from blog import urls as blog_urls
from . import views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^path/$', views.index),
    url(r'^user/$', views.display_good2),
    url(r'^meta/$', views.display_meta),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^contact/$', views.contact),
    url(r'^listbook/$', views.display_book),
    url(r'^publisher/$', views.PublisherList.as_view()),
    #dont include $ if not adding url again
    #like /music/list etc
    url(r'^music/', include(music_urls, namespace='music')),
    url(r'^blog/', include(blog_urls, namespace='blog')),
]
