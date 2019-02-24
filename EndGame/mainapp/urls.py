from django.urls import path, re_path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path("", views.index, name='index'),
    path("dashboard",views.dashboard, name="dashboard"),
    path("mycustomers",views.myCustomers, name="myCustomers")
]