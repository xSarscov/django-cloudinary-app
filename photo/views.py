from django.shortcuts import render
from . models import library
# Create your views here.

def index(request):

    photo = library.objects.all()

    return render(request, 'photo/index.html',
                  {'photo':photo}
                  
                  )