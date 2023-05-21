from django.shortcuts import render , redirect, get_object_or_404
from .models import *
from .forms import *
import random
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login




# Create your views here.


#listo productos en index
def index(request):
    tipo_id = request.GET.get('tipo_id')
    if tipo_id:
        productos_filtrados = Producto.objects.filter(tipo__id=tipo_id)
    else:
        productos_filtrados = Producto.objects.all()
        
    objeto_aleatorio = Producto.objects.all().order_by('?')

    data = {
        'listaProducto': productos_filtrados,
        'random': objeto_aleatorio,
    }

    return render(request, 'core/index.html', data)

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

def user_setting(request):
    return render(request,('core/user-setting.html'))


#######inicio crud del carrito

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

    total_carrito = 0  # Total general del carrito

    for item in items:
        total_producto = item.producto.precio * item.cantidad
        total_carrito += total_producto
        item.total_individual = total_producto

    return render(request, 'core/shoping-cart.html', {'productos': items, 'total_carrito': total_carrito})

def eliminar_producto_carrito(request, id):
    item = ItemCarrito.objects.get(id=id)
    item.delete()
    return redirect('ver_carrito')

##################fin crud carrito#####################


###########comienzo mostrar distintos valores de carrito################

def cantidad_items_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user, activo=True)
    items = ItemCarrito.objects.filter(carrito=carrito)
    cantidad_items = items.count()
    return JsonResponse({'cantidad_items': cantidad_items})

def obtener_total_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user, activo=True)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return JsonResponse({'total_carrito': total})


def obtener_precio_total(request, producto_id):
    carrito = Carrito.objects.first()  # Obtén el carrito que deseas utilizar

    try:
        item = carrito.itemcarrito_set.get(producto_id=producto_id)  # Obtén el item correspondiente al producto
        precio_total = item.producto.precio * item.cantidad  # Calcula el precio total
    except ItemCarrito.DoesNotExist:
        precio_total = 0  # Si no se encuentra el item, establece el precio total en 0

    context = {
        'precio_total': precio_total,
    }

    return render(request, 'shoping-cart.html', context)


def modificar_cantidad(request, item_id):
    item = ItemCarrito.objects.get(id=item_id)
    cantidad = int(request.POST['cantidad'])
    item.cantidad = cantidad
    item.save()
    return redirect('ver_carrito')
######fin de el area para mostrar los obejto de carrito##################



######################Registro##########################################
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado con exito")
            return redirect(to='index')
        data["form"] = formulario
    return render(request, 'registration/register.html', data)


def edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    else:
        form = UserEditForm(instance=user)

    return render(request, 'core/user-setting.html', {'form': form})
#####################Fin registro##################################

