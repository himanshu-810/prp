from django.urls import path
from .views import *

urlpatterns=[
    path('first',landing_home,name='first'),
    path("home_main",using_templates,name="home_main"),
    path("home",home_view,name="home")

]