from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('yes/', views.yes_page,name='yes'),
]
