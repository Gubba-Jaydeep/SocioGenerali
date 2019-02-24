from django.urls import path, re_path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path("", views.index, name='index'),
    path("dashboard",views.dashboard, name="dashboard"),
    path("mycustomers",views.myCustomers, name="myCustomers"),
    #mycustomers/pk
    re_path(r'^(?P<pk>[0-9]+)/$', views.customerDetail, name="customerDetail"),

]