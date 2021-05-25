from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cliente(request):
	return render(request, 'Cuenta_Cliente.html')
def Cliente_Perfil(request):
	return render(request, 'Cliente_Perfil.html')

def indexCliente(request):
	return render(request, 'indexCliente.html')
	
def novedades(request):
	return render(request, 'NovedadesCliente.html')

def colecciones(request):
	return render(request, 'ColeccionesCliente.html')

def promociones(request):
	return render(request, 'PromocionesCliente.html')
	