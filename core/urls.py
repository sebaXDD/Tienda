
from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('contact/',contact,name="contact"),
    path('blog/',blog,name="blog"),
    path('blogDetails/',blogdetails,name="blogDetails"),
    path('checkout/',checkout,name="checkout"),
    path('shopDetails/',shopdetails,name="shopDetails"),
    path('product-details/<int:id>/', product_details, name='product-details'),
    path('shopgrid/',shopgrid,name="shopGrid"),
    path('shopingCart/',shoppingcart,name="shopingCart"),


    path('agregar/<id>/', agregar_producto_carrito, name='agregar_carrito'),
    path('ver/', ver_carrito, name='ver_carrito'),
    path('eliminar/<id>/', eliminar_producto_carrito, name='eliminar_carrito'),
    path('cantidad_items_carrito/', cantidad_items_carrito, name='cantidad_items_carrito'),

    
    path('add-producto/',add,name="add-producto"),
    path('update-producto/<id>/',update,name="update-producto"),
    path('delete/<id>/',delete,name="delete"),
    path('user_setting/',user_setting,name="user_setting"),
    path('register/',register,name="register"),
]