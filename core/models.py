from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=25)
    
    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=3000)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True,blank=True)
    
    def __str__(self) :
        return self.nombre



class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)
    # Otros campos relevantes para tu carrito

    def __str__(self):
        return f"Carrito {self.id}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.carrito}"
    

class CosasUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customuser')
    imagen = models.ImageField(null=True,blank=True)
    si_quiere_ser_suscripto = models.BooleanField(default=False)
    monto_de_suscripcion = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fecha_de_pago = models.DateField(null=True, blank=True)
    fecha_de_inscripcion = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, args, **kwargs):
        if self.si_quiere_ser_suscripto is False:
            self.monto_de_suscripcion = None
            self.fecha_de_pago = None
        super().save(args, **kwargs)


    def str(self):
        return self.user.username
