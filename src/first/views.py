from django.shortcuts import render
from django.http import HttpResponse
from .templates import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_home(request):
    return HttpResponse("<h1>Hi This is himanshu</h1>")
def using_templates(request):
    return render(request,"first/website.html",{"name":"Himanshu"})

@login_required
def home_view(request):
    return render(request,'first/home.html')
