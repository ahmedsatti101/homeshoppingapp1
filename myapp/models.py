from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from decimal import Decimal
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
import uuid

PRODUCT_TYPES = (
    ('fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('dairy', 'Dairy'),
    ('bakery', 'Bakery'),
    ('meat', 'Meat'),
    ('fish', 'Fish'),
    ('drinks', 'Drinks'),
    ('snacks', 'Snacks'),
    ('frozen', 'Frozen'),
    ('household', 'Household'),
    ('other', 'Other'),
)

INVENTORY_STATUS = (
    ('IN_STOCK', 'In stock'),
    ('OUT_OF_STOCK', 'Out of stock'),
    ('LIMITED_STOCK', 'Limited stock'),
    ('PRE_ORDER', 'Pre-order'),
)

class Product(models.Model):
    title = models.CharField(max_length=20, help_text="Product name (e.g. Milk)")
    price = MoneyField(max_digits=5, decimal_places=2, default=0, default_currency='GBP', validators=[MinMoneyValidator(Decimal('0.00')), MaxMoneyValidator(Decimal('999.99'))])
    inventory_status = models.CharField(max_length=100, choices=INVENTORY_STATUS)
    type = models.CharField(max_length=100, choices=PRODUCT_TYPES)
    picture = models.ImageField(upload_to='img', default="")
    
    def __str__(self):
        return self.title
    
    def get_type_to_display(self):
        return PRODUCT_TYPES(self.type)
    
    def get_status_to_display(self):
        return INVENTORY_STATUS(self.inventory_status)
    
class Basket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return str(self.id)
    
class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="", related_name="items")
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, default="", related_name="basket_items")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.title