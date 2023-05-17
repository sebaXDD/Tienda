
from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('home/',home,name="home"),
    path('contact/',contact,name="contact"),
    path('blog/',blog,name="blog"),
    path('blogDetails/',blogdetails,name="blogDetails"),
    path('checkout/',checkout,name="checkout"),
    path('shopDetails/',shopdetails,name="shopDetails"),
    path('shopgrid/',shopgrid,name="shopGrid"),
    path('shopingCart/',shoppingcart,name="shopingCart"),


    path('agregar/<id>/', agregar_producto_carrito, name='agregar_carrito'),
    path('ver/', ver_carrito, name='ver_carrito'),
    path('eliminar/<id>/', eliminar_producto_carrito, name='eliminar_carrito'),

    
    path('add-producto/',add,name="add-producto"),
    path('update-producto/<id>/',update,name="update-producto"),
    path('delete/<id>/',delete,name="delete"),
]