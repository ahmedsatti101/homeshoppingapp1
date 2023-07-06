from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hello.html', {'name': 'Ahmed'})

def products(request):
    return HttpResponse("Products page.")

def basket(request):
    return HttpResponse("Basket page.")