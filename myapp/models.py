from django.db import models
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField
from decimal import Decimal
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

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
    
    def __str__(self):
        return self.title
    
    def get_type_to_display(self):
        return PRODUCT_TYPES(self.type)
    
    def get_status_to_display(self):
        return INVENTORY_STATUS(self.inventory_status)
    
class Customer(models.Model):
    first_name = models.CharField( max_length=100, default="")
    last_name = models.CharField( max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    phone_number = models.CharField(max_length=20, default="", validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    address_line_1 = models.CharField(max_length=100, default="")
    address_line_2 = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    postcode_validator = RegexValidator(regex=r'^[A-Z]{1,2}\d{1,2} ?\d[A-Z]{2}$', message="Enter a valid postcode in the format 'M20 2YH' or 'WX45 3GH'")
    postcode = models.CharField(max_length=8, default="", validators=[postcode_validator])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")