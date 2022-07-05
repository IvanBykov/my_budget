from django.urls import reverse

from buy.models import Magazine
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
        print(Magazine.objects.count())
        #41:22
