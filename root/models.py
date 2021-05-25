from django.db import models


class Newuser(models.Model):
	Email = models.CharField(max_length=150)
	Username = models.CharField(max_length=150)
	UserApellido = models.CharField(max_length=150)
	MartialStatus = models.CharField(max_length=150)
	Age = models.IntegerField()
	Pwd = models.CharField(max_length=150)
	Pwd1 = models.CharField(max_length=150)
	Gender = models.CharField(max_length=1)


class auth_user(models.Model):
	Age=models.IntegerField()
	
	

