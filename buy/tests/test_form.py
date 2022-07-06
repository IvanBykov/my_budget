from django.urls import reverse
from rest_framework import status

from buy.models import Magazine, Brand, Product, Buy
from buy.tests.test_models import Settings


class MagazineFormTest(Settings):
    def test_magazine_valid_form(self):
        magaz_count = Magazine.objects.count()
        self.assertEqual(1, magaz_count)
        form_data = {
            'name': 'Тестовый магазин',
            'address': 'тестовый адрес'
        }
        response = self.client.post(
            reverse('create-magazine'),
            data=form_data,
            follow=True
        )
        self.assertEqual(2, Magazine.objects.count())
        # 41:22
        saved_magaz = Magazine.objects.last()
        self.assertEqual('Тестовый магазин', saved_magaz.name)
        self.assertEqual('тестовый адрес', saved_magaz.address)

    def test_magazine_invalid_form(self):
        self.assertEqual(1, Magazine.objects.count())
        form_data = {
            'name': 'a'*51

        }
        response = self.client.post(
            reverse('create-magazine'),
            data=form_data,
            follow=True
        )
        self.assertEqual(1, Magazine.objects.count())

class BrandFormTest(Settings):
    def test_brand_valid_form(self):
        form_data = {
            'name': 'Тестовый брэнд'
        }
        response = self.client.post(
            reverse('create-brand'),
            data=form_data,
            follow=True
        )
        saved_brand = Brand.objects.last()
        self.assertEqual(2, Brand.objects.count())
        self.assertEqual('Тестовый брэнд', saved_brand.name)

class ProductFormTest(Settings):
    def test_product_valid_form(self):
        form_data = {
            'name': 'Тестовый продукт',
            #'category': self.category,
        }
        #надо проверить категорию
        response = self.client.post(
            reverse('create-product'),
            data=form_data,
            follow=True
        )
        self.assertEqual(2, Product.objects.count())
        saved_prod = Product.objects.last()
        self.assertEqual('Тестовый продукт', saved_prod.name)
        #self.assertEqual('', saved_prod.category.name)

class BuyFormTest(Settings):
    def test_buy_valid_form(self):
        self.assertEqual(1, Buy.objects.count())
        form_data = {
            #'product': self.product,
            'amount': '3',
            'date': '2022-05-20',
            #'unit': self.unit,
            #'magazine': self.magazine,
            'price': '12.5',
            #'brand': self.brand
        }
        response = self.client.post(
            reverse('create-buy'),
            data=form_data,
            follow=True
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, Buy.objects.count())
        saved_buy = Buy.objects.last()
        #self.assertEqual('', saved_buy.amount)
