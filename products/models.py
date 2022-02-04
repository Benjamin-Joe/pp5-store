"Models.py File For Products App"
from django.db import models


class Category(models.Model):
    "Model for categories on the website"
    name = models.CharField(max_length=200)

    class Meta:
        "Display correct spelling in admin section for categories"
        verbose_name_plural = "categories"

    def __str__(self):
        "Return the category name"
        return self.name


class Product(models.Model):
    "Model for the products on the website"
    category = models.ForeignKey(
                                'Category', related_name='product',
                                null=True, blank=True,
                                on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='001')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/', default='placeholder')
    description = models.TextField(default='Description Here')
    rating = models.DecimalField(
                                max_digits=6, decimal_places=2,
                                null=True, blank=True)

    class Meta:
        "Returns the correct spelling for product model in admin section"
        verbose_name_plural = "Products"

    def __str__(self):
        "Return the product title"
        return self.title
