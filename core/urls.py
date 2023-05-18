
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
    path('product-details/<int:id>/', product_details, name='product-details'),
    path('shopgrid/',shopgrid,name="shopGrid"),
    path('shopingCart/',shoppingcart,name="shopingCart"),


    path('add-producto/',add,name="add-producto"),
    path('update-producto/<id>/',update,name="update-producto"),
    path('delete/<id>/',delete,name="delete"),
]