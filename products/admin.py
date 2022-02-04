"Admin.py For Products App"
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    "Class for displaying products in admin section"
    list_display = (
        'title',
        'slug',
        'price',
        'rating',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    "Class for displaying categories in admin section"
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
