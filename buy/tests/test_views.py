from django.urls import reverse
from rest_framework import status

from buy.tests.test_models import Settings


class ListMagazineViewTest(Settings):
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        #print(response.context)
        #print(response.content.decode())

    def test_list_product_view(self):
        url = reverse('list-product')
        #print(url)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        #self.assertEqual('buy/list_product.html', response.template_name)
        #print(response.context.get('object_list'))
        self.assertEqual('продукт', response.context.get('object_list')[0].name)
