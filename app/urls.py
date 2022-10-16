from django.urls import path
from .views import home, menu, contacto

urlpatterns = [
    path('', home, name="home"),
    path('menu', menu, name="menu"),
    path('contacto', contacto, name="contacto"),
]