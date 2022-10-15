from itertools import product
from unicodedata import category
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("название", max_length=200, db_index=True)
    slug = models.SlugField("слаг", max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Категория" )
    name = models.CharField("название", max_length=200, db_index=True)
    slug = models.SlugField("слаг", max_length=200, db_index=True)
    image = models.ImageField("картинка", upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField("описание", blank=True)
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    avalible = models.BooleanField("Наличие", default=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name 

