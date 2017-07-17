from django.conf.urls import url
from . import views

app_name='portofolio'

urlpatterns = [
    url(r'^$', views.portofolio_list, name='portofolio_list'),
]
