from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Buy


# Create your views here.

class ListProduct(ListView):
    template_name = 'buy/list_product.html'
    model = Product

class ListBuy(ListView):
    template_name = 'buy/list_buy.html'
    model = Buy
