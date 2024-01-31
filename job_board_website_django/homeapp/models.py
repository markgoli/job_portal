# from email.policy import default
# from typing_extensions import Required
from django.db import models
from django.utils import timezone
from employee_app.models import Employee_model
# import datetime as dt

# Create your models here.


#   jobs model
class Jobs(models.Model):
    job_id               = models.AutoField( primary_key= True )
    job_title       = models.CharField( max_length= 200 )
    job_publication_date = models.DateField('publication date')
    job_subject_area     = models.CharField( max_length= 200)
    company   = models.CharField( max_length= 200 )
    job_description = models.TextField(max_length=2000)
    job_availability     = models.BooleanField( default=False )
    
    def __str__(self):
        return self.job_title
    
