from django.shortcuts import render
from django.template import loader
from .models import AdvisorDatabase, CustomerDatabase
from django.http import HttpResponseRedirect

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
    if request.COOKIES.get("loggedIn",None):
        db = AdvisorDatabase()
        user = db.getDataFromUname()
        return render(request, 'mainapp/home.html', {'user': user})
    else:
        return render(request, 'mainapp/login.html', {})

def logout(request):
    if request.COOKIES.get("loggedIn"):
        response = render(request,'mainapp/login.html',{})
        response.delete_cookie("userName")
        response.delete_cookie("loggedIn")
        return response
    else:
        render(request, 'mainapp/error.html', {})

def myCustomers(request):
    if request.COOKIES.get("loggedIn"):
        db = CustomerDatabase()
        customers= db.getData()[:10]
        return render(request, 'mainapp/customers.html' ,{'customers' : customers})
    else:
        return render(request, 'mainapp/login.html', {})

def customerDetail(request, pk):
    db = CustomerDatabase()
    customer = db.getDataFromPk(int(pk))
    return render(request,'mainapp/showdetails.html',{'customer' : customer})

def searchDetails(request):
    if request.COOKIES.get("loggedIn"):
        return render(request, 'mainapp/searchdetails.html',{})
    else:
        return render(request, 'mainapp/login.html', {})

def sendEmail(request):
    return HttpResponseRedirect("https://mail.google.com/mail/?view=cm&fs=1&to=neotrix1111@gmail.com&su=SUBJECT&body=BODY&bcc=someone.else@example.com")