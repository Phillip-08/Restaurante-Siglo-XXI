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
from .forms import CustomUserForm
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def get_queryset(self):
        producto = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            producto = producto.filter(nombre__contains = nombre)
        return producto
    
def home(request):
    return render(request, 'app/home.html')

def menu(request):
    return render(request, 'app/menu.html')

def registro(request):

    data= {
        'form':CustomUserForm()
    }

    if request.method == 'POST': 
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y rediridirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Te has registrado correctamenta")
            return redirect(to='home')
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

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


@permission_required('app.add_producto')
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

@permission_required('app.view_producto')
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

@permission_required('app.change_producto')    
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

@permission_required('app.delete_producto')
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