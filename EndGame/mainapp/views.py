from django.shortcuts import render
from django.template import loader
from .models import AdvisorDatabase, CustomerDatabase
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'mainapp/login.html', {})

def dashboard(request):
    #retrieving data from form and validation and redirection to dashboard page
    db =  AdvisorDatabase()
    dict_of_officials = db.getData()
    uname = request.GET['username']
    psw = request.GET['pass']
    try:
        if dict_of_officials[uname]==psw:
            return render(request,'mainapp/home.html',{'uname' : uname})
        else:
            return render(request,'mainapp/index.html',{})
    except Exception as ae:
        ctx= {'ae':ae}
        return render(request,'mainapp/error.html',ctx)

def myCustomers(request):
    db = CustomerDatabase()
    customers= db.getData()[:10]
    return render(request, 'mainapp/customers.html' ,{'customers' : customers})

def customerDetail(request):
    return render(request,'mainapp/idex.html',{})