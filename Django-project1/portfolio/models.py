from django.db import models

# Create your models here.
class person (models.Model):
    first_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    phone_number =models.CharField(max_length=70,blank=True,null=True)
    status=models.IntegerField(default=0)
