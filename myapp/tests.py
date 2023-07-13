from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Customer, Basket
        
class ProductTest(TestCase):
    def test_field_value(self):
        expected_value = 'Milk'
        my_model = Product(title=expected_value)
        acutal_value = my_model.title
        self.assertEqual(expected_value, acutal_value)
    
    def test_default_currency(self):
        #test that the default currency is GBP
        expected_value = 'GBP'
        my_model = Product()
        acutal_value = my_model.price_currency
        self.assertEqual(expected_value, acutal_value)
        
    def test_inventory_choices(self):
        #test that the inventory status takes the correct choices
        expected_value = 'IN_STOCK', 'OUT_OF_STOCK', 'LIMITED_STOCK', 'PRE_ORDER'
        my_model = Product(inventory_status=expected_value)
        acutal_value = my_model.inventory_status
        self.assertEqual(expected_value, acutal_value)
        
    def test_product_type_choices(self):
        #test that the product type takes the correct choices
        expected_value = 'fruit', 'Vegetable', 'dairy', 'bakery', 'meat', 'fish', 'drinks', 'snacks', 'frozen', 'household', 'other'
        my_model = Product(type=expected_value)
        acutal_value = my_model.type
        self.assertEqual(expected_value, acutal_value)
        
    def test_phone_number_format(self):
        #test that the phone number is in the correct format (e.g. +447123456789)
        expected_value = '+447123456789'
        my_model = Customer(phone_number=expected_value)
        actual_value = my_model.phone_number
        self.assertEqual(expected_value, actual_value)
        
    def test_postcode_format(self):
        expected_value = 'M20 2YH'
        my_model = Customer(postcode=expected_value)
        actual_value = my_model.postcode
        self.assertEqual(expected_value, actual_value)
        
class navgation_bar_exists(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_navbar_exists(self):
        url = reverse('myapp:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, '<nav>')
        self.assertContains(response, 'Home')
        self.assertContains(response, 'Products')
        self.assertContains(response, 'Basket')
        self.assertContains(response, 'Sign in')
        
class template_exists(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_basket_template(self):
        url = reverse('myapp:basket')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket.html')
        self.assertContains(response, 'Basket page.')
        
    def test_products_template(self):
        url = reverse('myapp:products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
        self.assertContains(response, 'Home')
        self.assertContains(response, 'Products')
        self.assertContains(response, 'Basket')
        self.assertContains(response, 'Sign in')
        
    def test_index_template(self):
        url = reverse('myapp:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Index page.')
        