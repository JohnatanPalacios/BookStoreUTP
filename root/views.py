from django.shortcuts import render
from root.models import Newuser
from django.contrib import messages


def Agregar_Administrador(request):
	return render(request, 'Cuenta_Root.html')


#usuario root predeterminado para inicio de sesion tiene como:
#Correo:paola.villada@utp.edu.co
#contraseña:APVO9977
#Importante no borrar ya que de aqui se pueden añadir usuarios root en caso de que se requiera
'''
def Userreg(request):
	if request.method=='POST':
		Email=request.POST['Email']
		Username=request.POST['Username']
		UserApellido=request.POST['UserApellido']
		MartialStatus=request.POST['MartialStatus']
		Age=request.POST['Age']
		Pwd=request.POST['Pwd']
		Pwd1=request.POST['Pwd1']
		Gender=request.POST['Gender']
		
		Newuser(Username=Username,UserApellido=UserApellido,Email=Email,Pwd=Pwd,Pwd1=Pwd1,Age=Age,Gender=Gender,MartialStatus=MartialStatus).save()
		messages.success(request,''+ request.POST['Username']+"-->Tu cuenta fue registada Exitosamente")
		return render(request,'Registro_Sesion_Root.html')
        #messages.success(request,'el nuevo usuario' + request.POST['Username']+' Es registrado')
        
    
	else:
		return render(request,'Registro_Sesion_Root.html')
'''		
def loginpage(request):
	if request.method=='POST':
		try:
			Userdetails=Newuser.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
			print('Username=',Userdetails)
			#request.session['Email']=Userdetails.Email
			return render(request,'Cuenta_Root.html')
		except Newuser.DoesNotExist as e:
			messages.success(request,'Username/Password invalid..')
	return render (request,'Inicio_Sesion_Root.html')

# Create your views here.
