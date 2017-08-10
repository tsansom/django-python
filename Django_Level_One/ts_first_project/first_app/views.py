from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('Hello World!')
    my_dict = {'insert_me': 'Below is a picture of my first guitar!'}
    return render(request, 'first_app/index.html', context=my_dict)
