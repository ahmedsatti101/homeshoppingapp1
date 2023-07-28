from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product, Basket
from .forms import SignUpForm
        
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
        self.assertContains(response, 'Home page.')

class user_login_form(TestCase):
    def test_login_form(self):
        url = reverse('myapp:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, '<input type="submit" value="Login">')
        self.assertContains(response, '<a href="{0}">Lost password?</a>'.format(reverse('password_reset')))
        self.assertContains(response, 'Don\'t have an account?')
        self.assertContains(response, '<a href="{0}">Create one</a>'.format(reverse('myapp:form')))
        
    def test_password_hashing(self):
        username = 'testuser'
        password = 'testpassword'
        user = User.objects.create_user(username=username, password=password)
        user_from_db = User.objects.get(username=username)
        self.assertNotEqual(user.password, password)
        self.assertTrue(user_from_db.check_password(password))
        self.client.login(username=username, password=password)
        self.assertTrue(self.client.session['_auth_user_id'])
        

class user_form_redirect(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_lost_password_redirect(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        
    def test_create_account_redirect(self):
        url = reverse('myapp:form')
        response = self.client.get(url)
        self.assertRedirects(response, '/accounts/login/?next=/myapp/form/')