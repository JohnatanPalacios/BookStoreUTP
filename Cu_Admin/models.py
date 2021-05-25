from django.db import models




class New(models.Model):
	Email=models.CharField(max_length=150)
	Username=models.CharField(max_length=150)
	
	Pwd=models.CharField(max_length=150)



