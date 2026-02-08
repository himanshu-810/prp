from django.db import models
from django.contrib.auth.models import User
from django import forms

from localflavor.us.models import USStateField,USZipCodeField   
from .utils import *

# Create your models here.


class Location(models.Model):
    address_1=models.CharField(max_length=128,blank=True)
    address_2=models.CharField(max_length=128,blank=True)
    city=models.CharField(max_length=64)
    state=USStateField(default="NY")
    zip_code=USZipCodeField(blank=True)

    def __str__(self):
        return f'{self.city} Location'


#models.CASCADE means -> on deletion of the parameter passed the feild also get deleted

class Profile(models.Model):#User-> This User is from the Admin User by Django
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    bio=models.CharField(max_length=256,blank=True)
    phone=models.CharField(max_length=12,blank=True)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
    