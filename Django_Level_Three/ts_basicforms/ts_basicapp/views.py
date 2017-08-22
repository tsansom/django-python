from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'ts_basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING
            print('VALIDATION SUCCESS')
            print('Name: {}\nEmail: {}\nText: {}'.format(form.cleaned_data['name'],
                                                         form.cleaned_data['email'],
                                                         form.cleaned_data['text']))

    return render(request, 'ts_basicapp/form_page.html', context={'form': form})
