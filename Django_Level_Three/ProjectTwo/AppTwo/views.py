from django.shortcuts import render
from AppTwo.models import User
from AppTwo import forms

# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

def users(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            User.objects.get_or_create(first_name=first_name,
                                       last_name=last_name,
                                       email=email)
            print('Success')
    return render(request, 'AppTwo/users.html', context={'form': form})
