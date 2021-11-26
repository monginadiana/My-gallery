from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    photo = CloudinaryField('photo')
    name =models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name