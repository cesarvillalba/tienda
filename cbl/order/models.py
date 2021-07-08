from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.forms import ModelForm

# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Cliente', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(
        Product, verbose_name='Producto', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(verbose_name='número',)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = "Carritos"


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(
        User, verbose_name='Cliente', on_delete=models.SET_NULL, null=True)
    code = models.CharField(verbose_name='Código', max_length=5, editable=False)
    first_name = models.CharField(verbose_name='Nombre', max_length=10)
    last_name = models.CharField(verbose_name='Apellido', max_length=10)
    phone = models.CharField(verbose_name='Teléfono', blank=True, max_length=20)
    tab_number = models.CharField(
        verbose_name='Número personal', blank=True, max_length=150)
    total = models.FloatField(verbose_name='Total',)
    status = models.CharField(verbose_name='Estado',
                              max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(verbose_name='Fecha y hora de pedido',auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = "Pedidos"
        ordering =['create_at']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'tab_number', 'phone']


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(
        Order, verbose_name='Pedido', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name='Cliente', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Producto', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='número',)
    price = models.FloatField(verbose_name='Precio',)
    amount = models.FloatField(verbose_name='El costo total del carrito')
    status = models.CharField(verbose_name='Estado',
                              max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Producto en carrito'
        verbose_name_plural = "Productos en el carrito"
