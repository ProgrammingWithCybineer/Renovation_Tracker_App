from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    #title of Renovation entry
    title = models.CharField(max_length=255)
    #house level working on
    houseLevel = models.CharField(max_length=255)
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
    #Entry added by
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #image loader option
    beforePhoto1 = models.ImageField(null=True, blank=True, upload_to="images/")
    beforePhoto2 = models.ImageField(null=True, blank=True, upload_to="images/")
    beforePhoto3 = models.ImageField(null=True, blank=True, upload_to="images/")
    beforePhoto4 = models.ImageField(null=True, blank=True, upload_to="images/")
    afterPhoto1 = models.ImageField(null=True, blank=True, upload_to="images/")
    afterPhoto2 = models.ImageField(null=True, blank=True, upload_to="images/")
    afterPhoto3 = models.ImageField(null=True, blank=True, upload_to="images/")
    afterPhoto4 = models.ImageField(null=True, blank=True, upload_to="images/") 
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
