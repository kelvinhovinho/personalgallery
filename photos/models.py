from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

from django.db.models.fields import CharField

# Create your models here.
class photos(models.Model):
    #title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    Description = models.CharField(max_length=200)
    location = models.ForeignKey(location,on_delete=True)


class location(models.Model):
    locationName = CharField(max_length=30)

    def saveLocation(self):
        self.saveLocation()

    def deleteLocation(self):
        self.deleteLocation()
    
class category(models.Model):
    categoryName = models.CharField(max_length=30)

    def saveCategory(self):
        self.saveCategory()

    @classmethod
    def updateCategory(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.categoryName
