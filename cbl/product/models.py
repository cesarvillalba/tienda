from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Nombre', max_length=50)
    keywords = models.CharField(verbose_name='Contraseña',max_length=255)
    description = models.TextField(verbose_name='Descripción', max_length=255)
    image=models.ImageField(verbose_name='Imagen', blank=True,upload_to='images/')
    status=models.CharField(verbose_name='Estado',max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural = "Categorías"


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(verbose_name='Nombre', max_length=150)
    keywords = models.CharField(verbose_name='Contraseña', max_length=255)
    description = models.TextField(verbose_name='Descripción',max_length=255)
    weight = models.PositiveIntegerField(verbose_name='Peso', default=0)
    image=models.ImageField(verbose_name='Imagen', upload_to='images/',null=False)
    price = models.DecimalField(verbose_name='Precio',max_digits=12, decimal_places=2,default=0)
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(verbose_name='Estado',max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name='Producto'
        verbose_name_plural = "Productos"






