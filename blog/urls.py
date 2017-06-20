from django.conf.urls import url
from .views import *

app_name='blog'

urlpatterns = [
	url(r'^$', post_list, name='post_list'),
]