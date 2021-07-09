from django.contrib import admin
from django.urls import path, include
from . import views
from .views import category_products, product_datail, product_resultado
from order import views as OrderView
from order.views import shopcart



urlpatterns = [
    path('', views.index, name = 'home'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_datail, name='product_datail'),
    path('home', views.product_resultado, name='product_resultado'),
    path('acerca_de', views.acerca_de, name='about'),
    path('contacto', views.contacto, name='contact'),
]
