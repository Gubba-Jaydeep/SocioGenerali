from django.urls import path, re_path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path("", views.index, name='index'),
    path("mainapp/dashboard",views.dashboard, name="dashboard"),
    path("mainapp/mycustomers",views.myCustomers, name="myCustomers")
]