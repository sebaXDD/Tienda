
from django.contrib import admin
from .models import *
from .models import CosasUser
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','stock','descripcion','tipo']
    search_fields=['nombre']
    list_per_page= 5
    list_filter=['tipo']
    list_editable=['precio','stock','descripcion','tipo']

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display=['carrito_id','producto_id','cantidad']
    search_fields=['producto_id']
    list_per_page= 5
    list_filter=['carrito_id']
    list_editable=['cantidad']

class CarritoAdmin(admin.ModelAdmin):
    list_display=['id','activo','fecha_creacion', 'usuario_id']
    search_fields=['id']
    list_per_page= 5
    list_filter=['fecha_creacion']
    list_editable=['activo']

class TipoProductoAdmin(admin.ModelAdmin):
    list_display=['id','descripcion']
    search_fields=['id']
    list_per_page= 5
    list_filter=['descripcion']
    list_editable=['descripcion']

class CosasUserAdmin(admin.ModelAdmin):
    list_display=['id','imagen','si_quiere_ser_suscripto','monto_de_suscripcion','fecha_de_pago']


admin.site.register(Producto,ProductoAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(ItemCarrito, ItemCarritoAdmin)
admin.site.register(CosasUser, CosasUserAdmin)