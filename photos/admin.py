from django.contrib import admin
from django.db.models.fields.files import ImageFileDescriptor
from .models import category, location, photos

# Register your models here.
admin.site.register(photos)
admin.site.register(location)
admin.site.register(category)

