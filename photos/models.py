from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class photos(models.Model):
    #title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    # posted_date = models.DateTimeField(auto_now_add=True)
    # description = models.CharField(max_length=200)
    # location = models.ForeignKey('location', on_delete=models.CASCADE)
    # category = models.ForeignKey('category', on_delete=models.CASCADE)

    # def saveImage(self):
    #     self.save()
    
    # def deleteaimage(self):
    #     self.delete()
