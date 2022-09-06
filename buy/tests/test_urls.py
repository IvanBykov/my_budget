from django.urls import reverse
from rest_framework import status


from buy.tests.test_models import Settings


class UrlsCaseTest(Settings):
    def test_index_get(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_buy_get(self):
        url = reverse('list-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_create_buy_get(self):
        url = reverse('create-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_product(self):
        url = reverse('list-product')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_product(self):
        url = reverse('create-product')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_brand(self):
        url = reverse('list-brand')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_brand(self):
        url = reverse('create-brand')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_category(self):
        url = reverse('list-category')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_category(self):
        url = reverse('create-category')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_unit(self):
        url = reverse('list-unit')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_unit(self):
        url = reverse('create-unit')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_magazine(self):
        url = reverse('list-magazine')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_magazine(self):
        url = reverse('create-magazine')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
