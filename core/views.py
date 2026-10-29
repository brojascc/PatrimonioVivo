from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'core/principal.html')

def login(request):
    return render(request, 'core/login.html')


def registrar(request):
    return render(request, 'core/registrar.html')