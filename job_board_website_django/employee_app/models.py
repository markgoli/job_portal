from django.db import models

# Create your models here.
class Employee_model(models.Model):
    Tel_No = models.IntegerField(primary_key=True )
    Employee_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(blank= True, max_length=50)
    active   = models.BooleanField(default=False)
    