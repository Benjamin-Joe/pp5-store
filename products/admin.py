"Admin.py For Products App"
from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

# Register your models here.
