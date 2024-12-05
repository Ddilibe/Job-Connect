from django.db import models
from django.db import models
import uuid
from core_root_api.security.user.models import User
# Create your models here.
class Job(models.Model):
    title=models.CharField(null=True,blank=True,max_length=1000)
    company_name=models.CharField(null=True,blank=True,max_length=1000)
    monthly_salary=models.CharField(null=True,blank=True,max_length=100)
    description=models.TextField(null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    no_of_opening=models.IntegerField(null=True,blank=True)
    application_starting_date = models.DateTimeField(null=True, blank=True)
    application_ending_date = models.DateTimeField(null=True, blank=True)




# Create your models here.
class ApplicationForm(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    cover_letter=models.TextField(null=True,blank=True)
    resume=models.FileField(upload_to='photos',null=True,blank=True)
    
# class RecruiterDashboard(models.Model):
