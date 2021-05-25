from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView
from usuario.forms import RegistroForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
	
		
class RegistroUsuario(CreateView):

	model=User
	template_name="Registro_Sesion.html"
	form_class=RegistroForm
	

	def get_success_url(self):
		return reverse('cliente')
	
		



		
	#messages.success(request,'Password invalid..')
	#return render(request,'Registro_Sesion.htmll')
	#messages.success(request,''+ request.POST['Username']+"-->Tu cuenta fue registada Exitosamente")
		


		