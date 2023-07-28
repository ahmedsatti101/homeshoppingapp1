from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Product, Basket, BasketItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    return render (request, 'index.html')

@login_required
def form(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
        
    context = {'form': form}
    return render(request, 'customer_form.html', context=context)

def loginPage(request):
    context = {}
    return render(request, 'registration/login.html', context)

def products(request):
    products = Product.objects.all()
    basket = request.session.get('basket', [])
    if request.method == 'POST':
        basket.append(request.POST['product_id'])
        request.session['basket'] = basket
        return redirect('myapp:products')
    num_basket_items = len(request.session.get('basket', []))
    context = {'num_basket_items': num_basket_items}
    return render(request, 'products.html', {'products': products})

def basket(request):
    if request.method == 'POST':
        request.session['basket'] = []
        return redirect('myapp:basket')
    
    basket = []
    product_ids = request.session.get('basket', [])
    for product_id in product_ids:
        product = Product.objects.get(pk=product_id)
        basket.append(product)
    return render(request, 'basket.html', {'basket': basket})

def add_to_basket(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = get_object_or_404(Product, pk=product_id)
        basket = request.session.get('basket', [])
        basket.append(request.POST['product_id'])
        request.session['basket'] = basket
    
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
        basketItem, created = BasketItem.objects.get_or_create(basket=basket, product=product)
        basketItem.quantity += 1
        basketItem.save()
        
    return redirect('myapp:basket')
        
 
def clear_basket(request):
    request.session['basket'] = []
    return redirect('myapp:basket')