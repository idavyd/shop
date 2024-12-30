from django.shortcuts import render
from .settings import BASE_DIR
from .forms import LoginForm
import requests


def dummy_home_view(request):
    return render(request, 'home.html', {'user': request.user.username})


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            response = requests.post(url='http://127.0.0.1:8000/api/token/',
                                     data={'username': username,
                                           'password': password},
                                     )
            access_token = response.json()['access_token']
            refresh_token = response.json()['refresh_token']
        else:
            pass
