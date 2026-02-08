from django.urls import path
from .views import *


urlpatterns=[
    path('user_login_form',users_login_form,name='user_login_form'),
    #path('user_register',register_view,name='register'),
    path('user_register',RegisterViewClass.as_view(),name='register'),
    path('logout',LogoutView,name='logout'),

    
]