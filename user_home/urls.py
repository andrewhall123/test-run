from django.conf.urls import url
from . import views

app_name='user_home'
urlpatterns=[
    url(r'^(?P<user>\w+)/$', views.user_home, name='user_home'),
    url(r'^edit/(?P<user>\w+)/$', views.travers, name='travers'),
]