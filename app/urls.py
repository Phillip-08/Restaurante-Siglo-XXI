from django.urls import path, include
from .views import home, menu, contacto, agregar_producto, listar_producto,modificar_producto, eliminar_producto, ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('menu/', menu, name="menu"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('api/', include(router.urls)),    
]