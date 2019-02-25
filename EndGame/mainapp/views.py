from django.shortcuts import render
from django.template import loader
from .models import AdvisorDatabase, CustomerDatabase
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mainapp/login.html', {})

def login(request):
    '''retrieving data from form and validation and redirection to dashboard page'''
    db = AdvisorDatabase()
    dict_of_officials = db.getData()
    uname = request.GET['username']
    psw = request.GET['pass']
    try:
        if dict_of_officials[uname] == psw:
            response=render(request, 'mainapp/home.html', {'uname': uname})
            response.set_cookie("loggedIn",True)
            response.set_cookie("userName", uname)
            return response
        else:
            return render(request, 'mainapp/index.html', {})
    except Exception as ae:
        ctx = {'ae': ae}
        return render(request, 'mainapp/error.html', ctx)

def dashboard(request):

    '''with open("./mklog.txt","wt") as f:
        f.write(str(request))'''
    if request.COOKIES.get("loggedIn"):
        return render(request, 'mainapp/home.html', {'uname': request.COOKIES.get("userName")})
    else:
        return render(request, 'mainapp/login.html', {})

def logout(request):
    request.COOKIES.clear()






def myCustomers(request):
    db = CustomerDatabase()
    customers= db.getData()[:10]
    return render(request, 'mainapp/customers.html' ,{'customers' : customers})

def customerDetail(request, pk):
    db = CustomerDatabase()
    customer = db.getDataFromPk(int(pk))
    return render(request,'mainapp/showdetails.html',{'customer' : customer})