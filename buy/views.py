from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Product, Buy, Brand, Category, Unit, Magazine
from .forms import BrandForm, BuyForm, ProductForm, CategoryForm, UnitForm, MagazineForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, 'buy/index.html')


def show_list_price(request):
    #prices = Buy.objects.all()
    prices = Buy.objects.filter(Q(product=5) & Q(date__gte='2022-05-23') & Q(date__lte='2022-05-24'))
    return render(request, 'buy/list_price.html', {
        'object_list': prices
    })


class ListProduct(ListView):
    template_name = 'buy/list_product.html'
    model = Product


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'buy/product.html'
    success_url = '/product'


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'buy/product.html'
    success_url = '/product'


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'buy/del_form.html'
    success_url = '/product'


class ListBuy(ListView):
    template_name = 'buy/list_buy.html'
    model = Buy


class CreateBuy(CreateView):
    model = Buy
    form_class = BuyForm
    template_name = 'buy/buy.html'
    success_url = '/buy'


class UpdateBuy(UpdateView):
    model = Buy
    form_class = BuyForm
    template_name = 'buy/buy.html'
    success_url = '/buy'


class DeleteBuy(DeleteView):
    model = Buy
    template_name = 'buy/del_form.html'
    success_url = '/buy'


class ListBrand(ListView):
    template_name = 'buy/list_brand.html'
    model = Brand


class CreateBrand(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'buy/brand.html'
    success_url = '/brand'


class UpdateBrand(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'buy/brand.html'
    success_url = '/brand'


class DeleteBrand(DeleteView):
    model = Brand
    template_name = 'buy/del_form.html'
    success_url = '/brand'


class ListCategory(ListView):
    template_name = 'buy/list_category.html'
    model = Category


class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'buy/category.html'
    success_url = '/category'


class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'buy/category.html'
    success_url = '/category'


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'buy/del_form.html'
    success_url = '/category'


class ListUnit(ListView):
    template_name = 'buy/list_unit.html'
    model = Unit


class CreateUnit(CreateView):
    model = Unit
    form_class = UnitForm
    template_name = 'buy/unit.html'
    success_url = '/unit'


class UpdateUnit(UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = 'buy/unit.html'
    success_url = '/unit'


class DeleteUnit(DeleteView):
    model = Unit
    template_name = 'buy/del_form.html'
    success_url = '/unit'


class ListMagazine(ListView):
    template_name = 'buy/list_magazine.html'
    model = Magazine


class UpdateMagazine(UpdateView):
    model = Magazine
    form_class = MagazineForm
    template_name = 'buy/magazine.html'
    success_url = '/magazine'


class DeleteMagazine(DeleteView):
    model = Magazine
    template_name = 'buy/del_form.html'
    success_url = '/magazine'


class CreateMagazine(CreateView):
    model = Magazine
    form_class = MagazineForm
    template_name = 'buy/magazine.html'
    success_url = '/magazine'
