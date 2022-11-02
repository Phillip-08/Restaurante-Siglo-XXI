from dataclasses import Field
from rest_framework import serializers
from .models import Producto, categoria

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'
class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombre")
    Categoria = categoriaSerializer(read_only=True)
    categoria_id: serializers.PrimaryKeyRelatedField(queryset = categoria.objects.all(), source="Categoria")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()
        
        if existe:
            raise serializers.ValidationError("Este menu ya existe")

        return value
    class Meta:
        model = Producto
        fields = '__all__'
        #exclude=[]
