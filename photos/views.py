from django.shortcuts import render
from .models import photos

# Create your views here.
def index(request):
    # importing photos and saving it in database
    photo = photos.objects.all()
    #adding context
    return render(request, 'index.html', {"photo": photo})
