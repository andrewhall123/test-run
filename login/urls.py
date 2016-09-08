from django.conf.urls import url
from . import views

app_name='login'
urlpatterns=[
    url(r'^$', views.logins, name='account_login'),
    url(r'^signup/$', views.signup, name='signup'),
    ]

