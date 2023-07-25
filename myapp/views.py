from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Product, Basket
from django.contrib.auth.decorators import login_required

def index(request):
    num_basket = Basket.objects.all().count()
    context = {'basket': basket}
    return render (request, 'index.html', context=context)

@login_required
def form(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
        
    context = {'form': form}
    return render(request, 'customer_form.html', context)

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
    return render(request, 'products.html', {'products': products})

def basket(request):
    basket = []
    product_ids = request.session.get('basket', [])
    for product_id in product_ids:
        product = Product.objects.get(pk=product_id)
        basket.append(product)
    return render(request, 'basket.html', {'basket': basket})

def add_to_basket(request):
    basket = request.session.get('basket', [])
    basket.append(request.POST['product_id'])
    request.session['basket'] = basket
    return redirect('myapp:basket')

def increment_basket_item(request, product_id):
    basket = request.session.get('basket', [])
    basket[product_id] = basket.get(product_id, 0) + 1
    request.session['basket'] = basket
    return redirect('myapp:basket')

def decrement_basket_item(request):
    basket = request.session.get('basket', [])
    if request.POST['product_id'] in basket:
        basket.remove(request.POST['product_id'])
    request.session['basket'] = basket
    return redirect('myapp:basket')

def remove_from_basket(request):
    basket = request.session.get('basket', [])
    basket = [item for item in basket if item != request.POST['product_id']]
    request.session['basket'] = basket
    return redirect('myapp:basket')