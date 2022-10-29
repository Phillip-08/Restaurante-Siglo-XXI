from dataclasses import Field
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class meta:
        model= Producto
        Field= '__all__'
