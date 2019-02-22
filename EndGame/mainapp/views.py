from django.shortcuts import render
from django.template import loader


# Create your views here.

def index(request):
    return render(request, 'mainapp/sih/login form/login.html', {})

def dashboard(request):
    #retrieving data from form and validation and redirection to dashboard page
    pass