from django.urls import path 
from . import views

urlpatterns = [
    #No borrar este path es de registro de root
    #path('register', views.Userreg),
    path('',views.loginpage),
    path('Agregar_Administrador', views.Agregar_Administrador, name='Agregar_Administrador'),
    
   
]