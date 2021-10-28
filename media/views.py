from django.shortcuts import render
from . models import Media
# Create your views here.

def home(requests):
    pictures = Media.objects.all()
    content = {
        'pictures' : pictures
    }

    return render(requests, 'home.html', content)