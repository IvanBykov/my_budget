from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UrlsCaseTest(APITestCase):
    def test_index_get(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_buy_get(self):
        url = reverse('list-buy')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
