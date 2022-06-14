from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Product, Buy, Brand, Category, Unit, Magazine
from .forms import BrandForm, BuyForm, ProductForm, CategoryForm, UnitForm, MagazineForm, GetPriceForm, GetDatePeriod
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import get_plot


# Create your views here.


def index(request):
    return render(request, 'buy/index.html')


def show_plot_price(request, pk: int):
    # x = [1, 5, 4, 7, 2]
    # y = [1, 2, 3, 4, 5, 6, 7]
    form = GetDatePeriod()
    if request.method == 'POST':
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        prices = Buy.objects.filter(Q(product=pk) & Q(date__gte=date_start) & Q(date__lte=date_end)).order_by(
            'date')
        y = [y.unit_price() for y in prices]
        x = [x.date for x in prices]
        chart = get_plot(x, y, f'{prices[0].product} за {prices[0].unit}')
        return render(request, 'buy/plot_price.html', {
            'chart': chart,
            'form': form,
            'pk': pk
        })
    #prices = Buy.objects.filter(Q(product=pk) & Q(date__gte='2022-05-20') & Q(date__lte='2022-05-27')).order_by('date')
    prices = Buy.objects.filter(Q(product=pk)).order_by('date')
    y = [y.unit_price() for y in prices]
    x = [x.date for x in prices]
    chart = get_plot(x, y, f'{prices[0].product} за {prices[0].unit}')
    return render(request, 'buy/plot_price.html', {
        'chart': chart,
        'form': form,
        'pk': pk
    })


def show_list_price(request):
    form = GetPriceForm()
    # prices = Buy.objects.all()
    if request.method == 'POST':
        product = request.POST['product']
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        prices = Buy.objects.filter(Q(product=product) & Q(date__gte=date_start) & Q(date__lte=date_end))
        return render(request, 'buy/list_price.html', {
            'object_list': prices,
            'form': form
        })
    return render(request, 'buy/list_price.html', {
        'form': form
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
