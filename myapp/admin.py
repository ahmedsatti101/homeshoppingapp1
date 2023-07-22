from django.contrib import admin
from .models import *

admin.site.register(Basket)
admin.site.register(BasketItem)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory_status', 'type')
    list_filter = ('title', 'price', 'inventory_status', 'type')
    search_fields = ('title', 'price', 'inventory_status', 'type')
    
admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number', 'city', 'postcode')
    list_filter = ('last_name', 'city', 'postcode')
    search_fields = ('last_name', 'phone_number', 'city', 'postcode')
    
admin.site.register(Customer, CustomerAdmin)