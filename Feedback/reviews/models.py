from django.db import models

# Create your models here.

class Review(models.Model):
    user_name=models.CharField(max_length=50)
    review_text=models.CharField(max_length=150)
    rating= models.IntegerField()