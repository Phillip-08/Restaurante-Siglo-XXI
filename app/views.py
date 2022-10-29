from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from .services import get_username
from .forms import ContactoForm, ProductoForm
from django.db import connection
from django.http import Http404
from django.contrib.auth import authenticate, login
from .models import Producto
from django.core.paginator import Paginator
from django.contrib import messages
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    
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

def agregar_producto(request):

    data={
        'form':ProductoForm
    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html',data)

def listar_producto(request):
    productos= Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data={
        'entity': productos,
        'paginator': paginator,
    }
    return render(request, 'app/producto/listar.html',data)
    
def modificar_producto(request, id):

    producto= get_object_or_404(Producto, id=id)

    data={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario= ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_producto")
        data["form"] = formulario
        
    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto= get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_producto")
    
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