from django.urls import path 
from . import views

urlpatterns = [
    path('Cliente', views.cliente, name='cliente'),
    path('Cliente_Perfil', views.Cliente_Perfil, name='Cliente_Perfil'),
    path('InicioCliente', views.indexCliente, name='InicioCliente'),
    path('NovedadesCliente', views.novedades, name='NovedadesCliente'),
    path('ColeccionesCliente', views.colecciones, name='ColeccionesCliente'),
    path('PromocionesCliente', views.promociones, name='PromocionesCliente'),
    
    

]