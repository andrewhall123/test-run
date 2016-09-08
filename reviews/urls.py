from django.conf.urls import url
from . import views

app_name='reviews'
urlpatterns=[
    url(r'^(?P<user>\w+)/$', views.reviews, name='reviews'),
    url(r'^all/(?P<user>\w+)/$', views.Review_List.as_view(), name='list'),
    url(r'^delete/(?P<pk>\d+)/$', views.pay_to_delete, name='delete_review'),
]