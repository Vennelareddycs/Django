from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

#many-to-many
class Country(models.Model):
    name=models.CharField(max_length=80)
    code=models.CharField(max_length=2)
    def __str__(self):
        return f"{self.name}, {self.code}"

    class Meta:
        verbose_name_plural="Countries"

class Address(models.Model):
    street= models.CharField(max_length=80)
    postal_code= models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city} "

    class Meta:
        verbose_name_plural="Address Entries" #change in admin page

#one-to-one relationship with adddress and author

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address=models.OneToOneField(Address, on_delete=models.CASCADE, null=True ) #no need to set related_name=author in one-to-one  because that will be the automatically assigned name,
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



class Book(models.Model):
    title= models.CharField(max_length=50) #class CharField(max_length=None, **options) A string field for small to large sized strings
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #class IntegerField(**options) 
    #default id with autoincrement is added for every db
    #author=models.CharField(null=True, max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") #that if author should be deleted, any related books should also be deleted,
    #That's a special field, which tells Django that the value inserted here is actually a pointer at an entry in the table for the authors
    is_bestselling=models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #Harry Potter 1 => harry-potter-1
    #it's automatically populated based on the title. Because the slug should always be the title just transformed to the slug version.
    published_countries = models.ManyToManyField(Country)
    #model urls
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    
    # def save(self, *args, **kwargs):  #Built-in save method for Overwriting Save
    #     self.slug = slugify(self.title) #It transforms a string to a slug.
    #     super().save(*args, **kwargs) #a slug is added for all our models.
    #     #For all the data entries we have in the database in the end.

    def __str__(self):
        return f"{self.title} ({self.rating}) "