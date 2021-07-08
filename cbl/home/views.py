from typing import ContextManager
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from product.models import Category, Product


# Create your views here.

def index(request):
    category = Category.objects.all()
    products_cold = Product.objects.all().order_by('category') [:3]
    products_cold2 = Product.objects.all().order_by('category') [3:10]
    context = {'category':category,'products_cold':products_cold,'products_cold2':products_cold2}
    return render(request,'home/home.html',context)

def product_resultado(request):
    busqueda = request.GET.get("buscar")
    #print(busqueda)
    category = Category.objects.all()
    products = Product.objects.filter(status = True)
    if busqueda:
       products = Product.objects.filter(
              Q(title__icontains = busqueda) |
              Q(description__contains = busqueda)
       ).distinct()

    #category = Category.objects.all()
    #products = Product.objects.objects.get(pk=id)
    context = {'products':products,'category':category}
    return render(request,'home/product_resultado.html',context)

def category_products(request,id,slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context={'products':products,'category':category}
    return render(request,'home/category_products.html',context)

def product_datail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    context={'product':product,'category':category}
    return render(request,'home/product_datail.html', context)




