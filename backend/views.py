from django.shortcuts import render
from .settings import BASE_DIR


def dummy_home_view(request):
    return render(request, 'home.html', {'user': request.user.username})


def login_view(request):
    return render(request, 'login.html', {})
