from django import forms
from .models import Brand, Buy, Product, Category, Unit, Magazine


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = '__all__'
