from django.contrib import admin
from .models import *

admin.site.register(Basket)
admin.site.register(BasketItem)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory_status', 'type')
    list_filter = ('title', 'price', 'inventory_status', 'type')
    search_fields = ('title', 'price', 'inventory_status', 'type')
    
admin.site.register(Product, ProductAdmin)