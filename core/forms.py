from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import *
from django.contrib.auth.models import User


class ProductoForm(ModelForm):
    
    nombre = forms.CharField(min_length=4,widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    precio = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Precio"}))
    stock = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Stock"}))
    descripcion = forms.CharField(min_length=10,max_length=200,widget=forms.Textarea(attrs={"rows":4}))

    class Meta:
        model = Producto
        #fields = ['nombre','precio','stock','descripcion','tipo']
        fields = '__all__'

        widgets = {
            'vencimiento' : forms.SelectDateWidget(years=range(1960,2024))
        }

class CustomUserCreationForm(UserCreationForm):
    pass



class CosasUserForm(forms.ModelForm):
    class Meta:
        model = CosasUser
        fields = ['imagen', 'si_quiere_ser_suscripto', 'monto_de_suscripcion', 'fecha_de_pago']
