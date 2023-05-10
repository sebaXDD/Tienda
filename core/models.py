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
    descripcion = models.CharField(max_length=300)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True,blank=True)
    
    def __str__(self) :
        return self.nombre