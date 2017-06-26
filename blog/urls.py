from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$',	views.post_detail,	name='post_detail'),
	url(r'^post/create/$', views.post_create, name='post_create'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/draft/$', views.post_draft, name='post_draft'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='publish'),
	url(r'^post/(?P<pk>\d+)/delete/$', views.post_remove, name='post_remove'),
]