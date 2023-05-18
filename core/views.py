from django.shortcuts import render , redirect, get_object_or_404
from .models import *
from .forms import *
import random
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.


#listo productos en index
def index(request):
    productosAll=Producto.objects.all()#select * from producto
    objeto_aleatorio = Producto.objects.all().order_by('?')
    data={
        'listaProducto':productosAll,
        'random':objeto_aleatorio
    }

    return render(request, 'core/index.html',data)

from django.shortcuts import render
from .models import Producto

def product_details(request, id):
    producto = Producto.objects.get(id=id)
    objeto_aleatorio = Producto.objects.all().order_by('?')
    context = {
        'producto': producto,
        'random':objeto_aleatorio
    }
    
    
    return render(request, 'core/shop-details.html', context)

    


def add(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # CAPTURAMOS LA INFO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # INSERT INTO producto VALUES()
            #data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add-product.html', data)


def update(request,id):
    producto = Producto.objects.get(id=id) # SELECT CON WHERE (BUSCAR)
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() # INSERT INTO producto VALUES()
            #data['msj'] = "Producto modificado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario # MOSTRAR EN LA VISTA LOS CAMBIOS

    return render(request, 'core/update-producto.html', data)

def delete(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="index")


def home(request):
    return render(request,('core/home.html'))


def contact(request):
    return render(request,('core/contact.html'))


def checkout(request):
    return render(request,('core/checkout.html'))

def blog(request):
    return render(request,('core/blog.html'))

def shopdetails(request):
    objeto_aleatorio = Producto.objects.all().order_by('?')
    data={
        'random':objeto_aleatorio
    }
    return render(request, 'core/shop-details.html', data)

@login_required
def shopgrid(request):
    return render(request, ('core/shop-grid.html'))

def shoppingcart(request):
    return render(request, ('core/shoping-cart.html'))

def blogdetails(request):
    return render(request, ('core/blog-details.html'))

def lista_collar(request):
    lista = Producto.objects.filter(tipo='collar').all()

    data = {
        'listaProductos' : lista
    }

    return render(request, ('core/pagina-collar.html'), data)

def lista_correa(request):
    lista = Producto.objects.filter(tipo='correa').all()

    data = {
        'listaProductos' : lista
    }

    return render(request, ('core/pagina-collar.html'), data)




def agregar_producto_carrito(request, id):
    producto = get_object_or_404(Producto, id= id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
    item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not item_created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user, activo=True)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'core/shoping-cart.html', {'productos': items, 'total': total})


def eliminar_producto_carrito(request, id):
    item = ItemCarrito.objects.get(id=id)
    item.delete()
    return redirect('ver_carrito')