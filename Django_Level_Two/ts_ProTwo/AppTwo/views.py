from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    my_dict = {'insert_help': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'user_records': user_list}

    return render(request, 'AppTwo/users.html', context=user_dict)
