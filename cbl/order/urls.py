from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('addtoshopcart/<int:id>', views.addtoshopcart, name = 'addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name = 'deletefromcart'),
    path('shopcart/', views.shopcart, name = 'shopcart'),
    path('orderproduct/', views.orderproduct, name = 'orderproduct'),
    
]
