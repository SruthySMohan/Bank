from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    address=models.TextField(default=True)
    email=models.EmailField(null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    branches = models.CharField(max_length=100,null=True,blank=True)
    account = models.CharField(max_length=100,null=True,blank=True)
    materialsprovided = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name