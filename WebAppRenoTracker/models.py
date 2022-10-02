from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
'''
Fields App needs
 house level, room, what was change/ renovated, 
 price, company used, before photos (limit 4), 
 after pics photos (limit 4)
 '''   
class newProject(models.Model):
    #title of website tab in browser
    #project_tag = models.CharField(max_length=255, default="No Tag")
    
    #title of Renovation entry
    project_title = models.CharField(max_length=255)
    #date project started    
    project_start_date = models.DateField()
    #house level working on
    house_Level = models.CharField(max_length=255)
    #room of house renovated
    room = models.CharField(max_length=255)
    #work performed
    work_Being_Done = models.CharField(max_length=1000)
    #cost of reno
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #company used
    company = models.CharField(max_length=255)
    #notes section
    notes = models.TextField()
    #date project completed  
    project_completion_date = models.DateField(null=True)
    #Entry added by. For database purposes
    updated_By = models.ForeignKey(User, on_delete=models.CASCADE)
    #image loader option
    before_Photo1 = models.ImageField(null=True, blank=True, upload_to="images/")
    before_Photo2 = models.ImageField(null=True, blank=True, upload_to="images/")
    before_Photo3 = models.ImageField(null=True, blank=True, upload_to="images/")
    before_Photo4 = models.ImageField(null=True, blank=True, upload_to="images/")
    after_Photo1 = models.ImageField(null=True, blank=True, upload_to="images/")
    after_Photo2 = models.ImageField(null=True, blank=True, upload_to="images/")
    after_Photo3 = models.ImageField(null=True, blank=True, upload_to="images/")
    after_Photo4 = models.ImageField(null=True, blank=True, upload_to="images/") 
    def __str__(self):
        return self.project_title + ' | ' + str(self.updated_By)
    
    # function to tell website where to redirect to after clicking submit, update, etc
    def get_absolute_url(self):
        #redirecting to details page
        #return reverse('project-details', args=(str(self.id)))
        #redirecting to home page
        return reverse('home')