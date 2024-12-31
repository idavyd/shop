from django.shortcuts import render, redirect
from .settings import BASE_DIR
from .forms import LoginForm
import requests
from rest_framework.status import HTTP_200_OK

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
            response = requests.post(url='http://127.0.0.1:8000/api/token/',
                                     data={'username': form.cleaned_data['username'],
                                           'password': form.cleaned_data['password']})
            if response.status_code is not HTTP_200_OK:
                print('INVALID USERNAME OR PASSWORD')
                return redirect('login')
            else:
                request.session['auth_token'] = response.json().get('access_token')
                return redirect('home')

