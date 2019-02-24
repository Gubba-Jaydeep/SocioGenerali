from django.shortcuts import render
from django.template import loader
from .models import AdvisorDatabase
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
    allCustomers={}

    return render(request, 'mainapp/index.html' ,allCustomers)