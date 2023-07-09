from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Product

def index(request):
    return render (request, 'index.html')

def form(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        
    context = {'form': form}
    return render(request, 'customer_form.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def basket(request):
    context = {}
    return render (request, 'basket.html', context)