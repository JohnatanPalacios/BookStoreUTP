
from django.shortcuts import render
from Cu_Admin.models import New
from django.contrib import messages


def Userreg(request):
	if request.method=='POST':
		Email=request.POST['Email']
		Username=request.POST['Username']
		Pwd=request.POST['Pwd']
		
		
		New(Username=Username,Email=Email,Pwd=Pwd).save()
		messages.success(request,"Administrador Creado")
		return render(request,'Cuenta_Root_Administrador.html')
        
        
    
	else:
		return render(request,'Cuenta_Root_Administrador.html')
	
def loginpage(request):
	if request.method=='POST':
		try:
			Userdetails=Newuser.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
			print('Username=',Userdetails)
			#request.session['Email']=Userdetails.Email
			return render(request,'Cuenta_Administrador.html')
		except Newuser.DoesNotExist as e:
			messages.success(request,'Username/Password invalid..')
	return render (request,'Inicio_Sesion_Administrador.html')

