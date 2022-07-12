from django import forms
from .models import Brand, Buy, Product, Category, Unit, Magazine


class DateInput(forms.DateInput):
    input_type = 'date'

class GetDatePeriod(forms.Form):
    date_start = forms.DateField(label='Начальная дата (ГГГГ-ММ-ДД)', widget=DateInput())
    date_end = forms.DateField(label='Конечная дата (ГГГГ-ММ-ДД)', widget=DateInput())


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        labels = {
            'name': 'Название'
        }


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'
        labels = {
            'product': 'Товар',
            'amount': 'Количество',
            'date': 'Дата',
            'unit': 'Единица измерения',
            'magazine': 'Магазин',
            'price': 'Стоимость',
            'brand': 'Брэнд'
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Название',
            'category': 'Категория'
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Название'
        }


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        labels = {
            'name': 'Название',
            'name_mini': 'Сокращенное название'
        }


class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = '__all__'
        labels = {
            'name': 'Название',
            'address': 'Адрес'
        }
