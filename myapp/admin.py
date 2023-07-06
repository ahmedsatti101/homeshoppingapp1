from django.contrib import admin
from .models import product_collection, Product

admin.site.register(product_collection)
admin.site.register(Product)