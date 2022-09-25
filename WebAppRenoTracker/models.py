from django.db import models
from django.urls import reverse

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
class renoProject(models.Model):
    #title of Renovation entry
    title = models.CharField(max_length=255)
    #image loader option
    #beforePhoto = models.ImageField(null=True, blank=True, upload_to="images/")
    #afterPhoto = models.ImageField(null=True, blank=True, upload_to="images/")
    #house level working on
    houseLevel = models.CharField(max_length=255)
    #room of house renovated
    room = models.CharField(max_length=255)
    #work performed
    workDone = models.CharField(max_length=255)
    #cost of reno
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #company used
    company = models.CharField(max_length=255)
    
