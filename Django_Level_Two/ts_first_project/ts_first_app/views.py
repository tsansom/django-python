from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':"Hello, I'm from ts_first_app!"}
    return render(request, 'ts_first_app/index.html', context=my_dict)
