from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product, Buy, Brand, Category, Unit, Magazine
from .forms import BrandForm, BuyForm, ProductForm, CategoryForm, UnitForm, MagazineForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, 'buy/index.html')


class ListProduct(ListView):
    template_name = 'buy/list_product.html'
    model = Product


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'buy/product.html'
    success_url = '/product'


def update_product(request, id_product: int):
    product = Product.objects.get(id=id_product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('list-product'))
    else:
        form = ProductForm(instance=product)
    return render(request, 'buy/product.html', context={'form': form})


class ListBuy(ListView):
    template_name = 'buy/list_buy.html'
    model = Buy


class CreateBuy(CreateView):
    model = Buy
    form_class = BuyForm
    template_name = 'buy/buy.html'
    success_url = '/buy'


def update_buy(request, id_buy: int):
    buy = Buy.objects.get(id=id_buy)
    if request.method == 'POST':
        form = BuyForm(request.POST, instance=buy)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse("list-buy"))
    else:
        form = BuyForm(instance=buy)
    return render(request, 'buy/buy.html', context={'form': form})


class ListBrand(ListView):
    template_name = 'buy/list_brand.html'
    model = Brand


class CreateBrand(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'buy/brand.html'
    success_url = '/brand'


def update_brand(request, id_brand: int):
    brand = Brand.objects.get(id=id_brand)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.cleaned_data
            form.save()
            redirect_urls = reverse("list-brand")
            return HttpResponseRedirect(redirect_urls)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'buy/brand.html', context={'form': form})


class ListCategory(ListView):
    template_name = 'buy/list_category.html'
    model = Category


class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'buy/category.html'
    success_url = '/category'


def update_category(request, id_category: int):
    category = Category.objects.get(id=id_category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('list-category'))
    else:
        form = CategoryForm(instance=category)
    return render(request, 'buy/category.html', context={'form': form})


class ListUnit(ListView):
    template_name = 'buy/list_unit.html'
    model = Unit


class CreateUnit(CreateView):
    model = Unit
    form_class = UnitForm
    template_name = 'buy/unit.html'
    success_url = '/unit'


def update_unit(request, id_unit: int):
    unit = Unit.objects.get(id=id_unit)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('list-unit'))
    else:
        form = UnitForm(instance=unit)
    return render(request, 'buy/unit.html', context={'form': form})


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
    #form_class = MagazineForm
    # context_object_name = 'form'
    template_name = 'buy/magazine.html'
    success_url = '/magazine'


def update_magazine(request, id_magazine: int):
    magazine = Magazine.objects.get(id=id_magazine)
    if request.method == 'POST':
        form = MagazineForm(request.POST, instance=magazine)
        if form.is_valid():
            # form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('list-magazine'))
    else:
        form = MagazineForm(instance=magazine)
    return render(request, 'buy/magazine.html', context={'form': form})


def del_magazine(request, id_magazine: int):
    magazine = Magazine.objects.get(id=id_magazine)
    if request.method == 'POST':
        magazine.delete()
        return HttpResponseRedirect(reverse('list-magazine'))
    form = MagazineForm(instance=magazine)
    return render(request, 'buy/magazine.html', context={'form': form})


class CreateMagazine(CreateView):
    model = Magazine
    form_class = MagazineForm
    template_name = 'buy/magazine.html'
    success_url = '/magazine'
