from django.db import models

# Create your models here.
class Users(models.Model):
    first_name= models.CharField("first_name", max_length=30, blank=True,null=True)
    last_name= models.CharField("last_name", max_length=30, blank=True, null=True)
    email = models.EmailField("Email", max_length=30)
    password= models.CharField("Password",max_length=25)
    ph_no = models.IntegerField("Phn_no", null=True)
    created_at=models.DateTimeField(auto_now_add=True )