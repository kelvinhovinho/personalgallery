from django.shortcuts import render
# from .models import photos

# Create your views here.
def index(request):
    # importing photos and saving it in database
    # photo = photos.objects.all()
    #adding context
    # ctx = {'photo':photo}
    return render(request, 'index.html')
