from django.contrib import admin
from django.db.models.fields.files import ImageFileDescriptor
from .models import photos

# Register your models here.
admin.site.register(photos)

