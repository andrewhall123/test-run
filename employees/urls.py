from django.conf.urls import url
from . import views

app_name='employees'
urlpatterns=[
    url(r'^$', views.employee.as_view(), name='employee'),
    url(r'^by_review', views.employee_by_review, name='review'),
]