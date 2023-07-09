from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.form, name="form"),
    path("products/", views.products, name="products"),
    path("basket/", views.basket, name="basket"),
]