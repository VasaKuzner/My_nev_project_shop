

from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категори]'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField() # Це поле для зберігання залишків цього продукту
    available = models.BooleanField(default=True) # ТОбто is-acnive
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт '
        verbose_name_plural = 'Продукти '
        ordering = ('name',)
        index_together = (('id', 'slug'),) # Ми визначаємо цей шдекс оскільки ми плануємо запросити продуск за допомогою id i slug

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])

class ProducPhoto(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,  on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/$d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час змнін")
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Фотографія'
        verbose_name_plural = 'Фотографії '
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.product.id, self.slug])
