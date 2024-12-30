from django.shortcuts import render


def dummy_home_view(request):
    return render(request, 'home.html', {})
