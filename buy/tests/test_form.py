from django.urls import reverse

from buy.models import Magazine, Brand, Product
from buy.tests.test_models import Settings


class MagazineFormTest(Settings):
    def test_valid_form(self):
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


class BrandFormTest(Settings):
    def test_valid_form(self):
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
    def test_valid_form(self):
        form_data = {
            'name': 'Тестовый продукт'
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

