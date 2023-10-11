from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=50) #class CharField(max_length=None, **options) A string field for small to large sized strings
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #class IntegerField(**options) 
    #default id with autoincrement is added for every db
    author=models.CharField(null=True, max_length=100)
    is_bestselling=models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #Harry Potter 1 => harry-potter-1
    #it's automatically populated based on the title. Because the slug should always be the title just transformed to the slug version.
    #model urls
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    
    # def save(self, *args, **kwargs):  #Built-in save method for Overwriting Save
    #     self.slug = slugify(self.title) #It transforms a string to a slug.
    #     super().save(*args, **kwargs) #a slug is added for all our models.
    #     #For all the data entries we have in the database in the end.

    def __str__(self):
        return f"{self.title} ({self.rating}) "