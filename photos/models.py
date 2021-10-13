from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE




class location(models.Model):
    locationName = models.CharField(max_length=30, default=None)

    def saveLocation(self):
        self.save()

    def deleteLocation(self):
        self.delete()
    

    @classmethod
    def updateLocation(cls,id,value):
        cls.objects.filter(id=id).update(image = value)
    
    def __str__(self):
        return self.locationName

class category(models.Model):
    categoryName = models.CharField(max_length=30, default=None)

    def saveCategory(self):
        self.save()
    def deleteCategory(self):
        self.delete
    

    @classmethod
    def updateCategory(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.categoryName


# Create your models here.
class photos(models.Model):
    #title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    Description = models.CharField(max_length=200, default=None)
    location = models.ForeignKey(location,on_delete=CASCADE,default=None)
    category = models.ForeignKey(category,on_delete=CASCADE, default=None)


    def saveImage(self):
        self.save()

    def deleteImage(self):
        self.delete()
    
    @classmethod
    def updateImage(cls,id,value):
        cls.objects.filter(id=id).update(image=value)


    @classmethod
    def getImageById(cls,id):
        image = cls.objects.filter(id=id).all()
        return image


    @classmethod
    def seachphoto(cls,category):
        category = cls.objects.filter(photos_categoru_categoryName_icontains = category)
        return category
    @classmethod
    def filterphotosByLocation(cls,location):
        location = cls.objects.filter(photoLocation_LocationName = category)
        return location

    def __str__(self):
        return self.title



    