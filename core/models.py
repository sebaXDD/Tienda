from django.db import models

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
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    # Otros campos relevantes para tu carrito

    def __str__(self):
        return f"Carrito {self.id}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.carrito}"