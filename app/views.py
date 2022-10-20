from django.shortcuts import render
from .services import get_username
from .forms import ContactoForm
from django.db import connection
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def menu(request):
    return render(request, 'app/menu.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje Enviado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

#API
def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'hello_user.html', context)

def hello_user(requests):
    params = { 'order': 'desc' }

    context = {
        'name': get_username(params)
    }
    return render(requests, 'hello_user.html', context)