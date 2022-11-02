from dataclasses import field, fields
from email.mime import image
from django import forms
from django import forms
from django.contrib.auth.models import User
from .models import Contacto, Producto, Registro
from django.contrib.auth.forms import UserCreationForm
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=500, max_value=250000)
    imagen = forms.ImageField(required=True, validators=[MaxSizeFileValidator(max_file_size = 5)])

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact = nombre).exists()

        if existe:
            raise ValidationError(" Este Menu ya existe")

        return nombre

    class Meta:
        model = Producto
        fields= '__all__'


#class DetalleCompraForm