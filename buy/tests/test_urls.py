from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


#class UrlsCaseTest(APITestCase):
from buy.tests.test_models import Settings


class UrlsCaseTest(Settings):
    def test_index_get(self):
        #print('test_index_get')
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        #print(response.template_name)
        #print(dir(response))

    #def test_list_price_get(self):
    #    print(self.product.pk)
    #    url = reverse('list-price')
    #    print(url)
    #    response = self.client.get(url)
    #    self.assertEqual(status.HTTP_200_OK, response.status_code)
#
    #def test_plot_price_get(self):
    #    url = reverse('plot-price')
    #    response = self.client.get(url)
    #    self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_buy_get(self):
        #print('test_list_buy_get')
        url = reverse('list-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        #print(dir(response))
        #print(response.template_name)

    #def test_update_buy_get(self):
    #    #print('test_list_buy_get')
    #    url = reverse('update-buy')
    #    response = self.client.get(url)
    #    self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_buy_get(self):
        url = reverse('create-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
