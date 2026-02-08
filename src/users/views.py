from django.shortcuts import render,redirect
from django.http import HttpResponse
from .templates import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.


def users_login_form(request):
    if request.method=='POST':
        login_form=AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'You are now logged in as {username}')
                return redirect('home')#home is the name in urls.py
            else:
                messages.error(request,f'user {username} not registered \n Please Sign In!')
        else:
            messages.error(request,f'user not registered \n Please Sign In!')
                
    elif request.method=='GET':
        login_form=AuthenticationForm()
        #inside the dict we are sending thr values to the form or request or template
    
    return render(request,"users/login.html",{"name":"users","login_form_dict":login_form})


# def register_view(request):
    # register_form=UserCreationForm()
    # return render(request,"users/register.html",{"user_register_form":register_form})

class RegisterViewClass(View):
    def get(self,request):
        register_form_get=UserCreationForm()
        return render(request,"users/register.html",{"user_register_form":register_form_get})
    def post(self,request):
        
        register_form = UserCreationForm(data=request.POST)   
        
        if register_form.is_valid():
            user=register_form.save()#value save in DB
            user.refresh_from_db()#User variable refreshed with latest value
            user.is_staff=True
            login(request,user)
            messages.success(request,f'User {user.username} Registered Successfully')
            user_login_form = request.POST.get("user_login_form")
            
            return render(request,'users/login.html',{"user_login_form":user_login_form})
        else:
            messages.error(request,f'user not registered!!!')
            register_form_get=UserCreationForm()
            return render(request,"users/register.html",{"user_register_form":register_form_get})

@login_required
def LogoutView(request):
    
    logout(request)
    return redirect('home_main')
    