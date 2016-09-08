from django.conf.urls import url
from . import views

app_name='payment'
urlpatterns=[
    url(r'^(?P<pk>\d+)/$', views.pay, name='pay'),
]