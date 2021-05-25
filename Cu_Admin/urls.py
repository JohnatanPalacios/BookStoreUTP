from django.urls import path 
from . import views

urlpatterns = [
    #No borrar este path es de registro de root
    path('registe', views.Userreg),
    path('inicio',views.loginpage),
    
    
   
]
