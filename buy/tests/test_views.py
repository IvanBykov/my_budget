from django.urls import reverse
from rest_framework import status

from buy.tests.test_models import Settings


class ListProductViewTest(Settings):
    def test_list_product_view(self):
        url = reverse('list-product')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('продукт', response.context.get('object_list')[0].name)
        self.assertEqual('buy/list_product.html', response.template_name[0])


class CreateProductViewTest(Settings):
    def test_create_product_view(self):
        url = reverse('create-product')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/product.html', response.template_name[0])

class UpdateProductViewTest(Settings):
    def test_update_product_view(self):
        url = reverse('update-product', args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/product.html', response.template_name[0])

class DeleteProductViewTest(Settings):
    def test_delete_product_view(self):
        url = reverse('del-product', args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/del_form.html', response.template_name[0])

class ListBuyViewTest(Settings):
    def test_list_buy_view(self):
        url = reverse('list-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

class CreateBuyViewTest(Settings):
    def test_create_buy_view(self):
        url = reverse('create-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/buy.html', response.template_name[0])

class UpdateBuyViewTest(Settings):
    def test_update_buy_view(self):
        #print(self.buy.pk)
        url = reverse('update-buy', args=[self.buy.pk])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/buy.html', response.template_name[0])

class DeleteBuyViewTest(Settings):
    def test_delete_buy_view(self):
        url = reverse('del-buy', args=[self.buy.pk])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/del_form.html', response.template_name[0])

class ListBrandViewTest(Settings):
    def test_list_brand_view(self):
        url = reverse('list-brand')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('buy/list_brand.html', response.template_name[0])

class LoadBuyViewTest(Settings):
    def test_load_buy_view(self):
        url = reverse('load_buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
