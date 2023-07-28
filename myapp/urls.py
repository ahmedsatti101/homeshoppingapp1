from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.form, name="form"),
    path('login/', views.loginPage, name="login"),
    path("products/", views.products, name="products"),
    path("basket/", views.basket, name="basket"),
    path("add_to_basket/", views.add_to_basket, name="add_to_basket"),
    path("clear_basket/", views.clear_basket, name="clear_basket"),
]