from django.contrib import admin
from .models import *

# Register your models here.

class Categoriaadmin(admin.ModelAdmin):
    list_display: ["nombre"]
    search_fields: ["nombre"]

admin.site.register(categoria)
admin.site.register(Producto)
admin.site.register(Contacto)
