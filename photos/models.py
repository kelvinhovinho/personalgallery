from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class photos(model.Models):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
