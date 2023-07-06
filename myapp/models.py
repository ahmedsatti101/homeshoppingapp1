from django.db import models

class product_collection(models.Model):
    title = models.CharField(max_length=30, help_text="Add product category")
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=20, help_text="Product name (e.g. Milk)")
    price = models.IntegerField(help_text="Enter price")
    inventory_status = models.CharField(max_length=30, help_text="Is product available or not?")
    type = models.ForeignKey(product_collection, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)