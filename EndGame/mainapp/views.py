from django.shortcuts import render
from django.template import loader
from .models import AdvisorDatabase


# Create your views here.

def index(request):
    return render(request, 'mainapp/login.html', {})

def dashboard(request):
    #retrieving data from form and validation and redirection to dashboard page
    db =  AdvisorDatabase()
    dict_of_officials = db.getData()
    uname = request.POST['username']
    psw = request.POST['pass']
    try:
        if dict_of_officials[uname]==psw:
            return render(request,'mainapp/customers.html',{})
        else:
            return render(request,'mainapp/index.html',{})
    except:
        return render(request,'mainapp/error.html',{})