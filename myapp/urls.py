from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.form, name="form"),
    path("products/", views.products, name="products"),
    path("basket/", views.basket, name="basket"),
    path("add_to_basket/", views.add_to_basket, name="add_to_basket"),
    path("increment_basket_item/", views.increment_basket_item, name="increment_basket_item"),
    path("decrement_basket_item/", views.decrement_basket_item, name="decrement_basket_item"),
    path("remove_from_basket/", views.remove_from_basket, name="remove_from_basket")
]