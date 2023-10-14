from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to = "data")
    #image= models.FileField(upload_to="images") #specify the loc to upload in settings 
    