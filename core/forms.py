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
    nueva_contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'nueva_contraseña']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'cosasuser'):
            cosas_user = self.instance.cosasuser
            self.fields['imagen'] = forms.ImageField(required=False)
            self.fields['si_quiere_ser_suscripto'] = forms.BooleanField(required=False)
            self.fields['monto_de_suscripcion'] = forms.DecimalField(
                max_digits=8,
                decimal_places=2,
                required=False
            )
            self.fields['fecha_de_pago'] = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
            self.fields['fecha_de_inscripcion'] = forms.DateTimeField(disabled=True, required=False, widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))
            self.initial['imagen'] = cosas_user.imagen
            self.initial['si_quiere_ser_suscripto'] = cosas_user.si_quiere_ser_suscripto
            self.initial['monto_de_suscripcion'] = cosas_user.monto_de_suscripcion
            self.initial['fecha_de_pago'] = cosas_user.fecha_de_pago
            self.initial['fecha_de_inscripcion'] = cosas_user.fecha_de_inscripcion

    def clean(self):
        cleaned_data = super().clean()
        nueva_contraseña = cleaned_data.get('nueva_contraseña')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')

        if nueva_contraseña and confirmar_contraseña and nueva_contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")

        return cleaned_data

