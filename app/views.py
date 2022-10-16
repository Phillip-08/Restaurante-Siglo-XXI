from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def menu(request):
    return render(request, 'app/menu.html')

def contacto(request):
    return render(request, 'app/contacto.html')