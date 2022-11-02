from django.contrib import admin
from .models import *
from .forms import ProductoForm

# Register your models here.

class Categoriaadmin(admin.ModelAdmin):
    list_display: ["nombre"]
    search_fields: ["nombre"]
    form = ProductoForm

admin.site.register(categoria)
admin.site.register(Producto)
admin.site.register(Contacto)
