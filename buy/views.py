from django.db.models import Q, Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from datetime import datetime

from .libs.import_buy import import_buy, parse_name
from .models import Product, Buy, Brand, Category, Unit, Magazine, BuyTmp
from .forms import BrandForm, BuyForm, ProductForm, CategoryForm, UnitForm, MagazineForm, GetDatePeriod
from buy.libs.utils import get_plot, delta_price


def index(request):
    return render(request, 'buy/index.html')


def show_plot_price(request, pk: int):
    if request.method == 'POST':
        form = GetDatePeriod(request.POST)
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
    else:
        form = GetDatePeriod()
    prices = Buy.objects.filter(Q(product=pk)).order_by('date')
    y = [y.unit_price() for y in prices]
    x = [x.date for x in prices]
    chart = get_plot(x, y, f'{prices[0].product} за {prices[0].unit}')
    return render(request, 'buy/plot_price.html', {
        'chart': chart,
        'form': form,
        'pk': pk
    })


def show_list_price(request, pk: int):
    if request.method == 'POST':
        form = GetDatePeriod(request.POST)
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        prices = Buy.objects.filter(Q(product=pk) & Q(date__gte=date_start) & Q(date__lte=date_end))
        return render(request, 'buy/list_price.html', {
            'date_start': datetime.strptime(date_start, '%Y-%m-%d').date(),
            'date_end': datetime.strptime(date_end, '%Y-%m-%d').date(),
            'delta_price': delta_price(prices),
            'object_list': prices,
            'form': form,
            'pk': pk,
        })
    else:
        form = GetDatePeriod()
    prices = Buy.objects.filter(Q(product=pk)).order_by('date')
    return render(request, 'buy/list_price.html', {
        'date_start': prices[0].date,
        'date_end': prices[len(prices) - 1].date,
        'delta_price': delta_price(prices),
        'object_list': prices,
        'form': form,
        'pk': pk,
    })


def show_period_expenses(request):
    if request.method == 'POST':
        form = GetDatePeriod(request.POST)
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        buy = Buy.objects.filter(Q(date__gte=date_start) & Q(date__lte=date_end)).order_by('date')
        sum_in_period = Buy.objects.filter(Q(date__gte=date_start) & Q(date__lte=date_end)).aggregate(Sum('price'))
        return render(request, 'buy/list_buy.html', {
            'date_start': datetime.strptime(date_start, '%Y-%m-%d').date(),
            'date_end': datetime.strptime(date_end, '%Y-%m-%d').date(),
            'object_list': buy,
            'form': form,
            'sum': sum_in_period,
        })
    else:
        form = GetDatePeriod()
    return render(request, 'buy/list_buy.html', {
        'form': form,
    })


class ListProduct(ListView):
    template_name = 'buy/list_product.html'
    paginate_by = 20
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
    paginate_by = 20
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
    paginate_by = 20
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
    paginate_by = 20
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
    paginate_by = 20
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
    paginate_by = 20
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


def storage_file(file):
    with open('buy_tmp/new_email.eml', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


class LoadBuy(View):
    def get(self, request):
        magazines = Magazine.objects.all()
        return render(request, 'buy/load_buy.html', context={
            'magazines': magazines
        })

    def post(self, request):
        storage_file(request.FILES['email'])
        products = import_buy()
        # date = request.POST['date']
        magazine = Magazine.objects.get(pk=request.POST['fav_magazine'])
        querysetlist = []
        for product in products:
            querysetlist.append(BuyTmp(name=product[0],
                                       amount=product[1],
                                       price_unit=product[2],
                                       price_buy=product[3],
                                       # date=date,
                                       # date=product[4],
                                       date=product[4][6:10]+'-'+product[4][3:5]+'-'+product[4][:2],
                                       magazine=magazine))
        BuyTmp.objects.bulk_create(querysetlist)
        # BuyTmp(name=product[0], amount=product[1], price_unit=product[2], price_buy=product[3], date=date,
        #       magazine=magazine).save()
        return render(request, 'buy/load_buy.html', context={
            'message': 'данные загружены'
        })


def insert_buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid() and request.POST['select'] == 'add':
            form.save()
            buy_tmp = BuyTmp.objects.first()
            buy_tmp.delete()
            if len(BuyTmp.objects.all()) == 0:
                return render(request, 'buy/import_buy.html', context={
                    'message': 'данные для импорта отсутствуют'
                })
            buy_tmp = BuyTmp.objects.first()
            name_split = parse_name(buy_tmp.name)
            brand = Brand.objects.filter(name=name_split['brand']).first()
            unit = Unit.objects.filter(name_mini=name_split['unit']).first()
            product = Product.objects.filter(name=name_split['name']).first()
            buy = Buy(amount=buy_tmp.amount * name_split['weight'],
                      price=buy_tmp.price_buy,
                      date=buy_tmp.date,
                      magazine=buy_tmp.magazine,
                      brand=brand,
                      unit=unit,
                      product=product
                      )
            form = BuyForm(instance=buy)
            return render(request, 'buy/import_buy.html', context={
                'form': form,
                'message': buy_tmp.name,
            })
        elif form.is_valid() and request.POST['select'] == 'skip':
            buy_tmp = BuyTmp.objects.first()
            buy_tmp.delete()
    if len(BuyTmp.objects.all()) == 0:
        return render(request, 'buy/import_buy.html', context={
            'message': 'данные для импорта отсутствуют'
        })
    buy_tmp = BuyTmp.objects.first()
    name_split = parse_name(buy_tmp.name)
    brand = Brand.objects.filter(name=name_split['brand']).first()
    unit = Unit.objects.filter(name_mini=name_split['unit']).first()
    product = Product.objects.filter(name=name_split['name']).first()
    buy = Buy(amount=buy_tmp.amount * name_split['weight'],
              price=buy_tmp.price_buy,
              date=buy_tmp.date,
              magazine=buy_tmp.magazine,
              brand=brand,
              unit=unit,
              product=product)
    form = BuyForm(instance=buy)
    return render(request, 'buy/import_buy.html', context={
        'form': form,
        'message': buy_tmp.name,
    })
