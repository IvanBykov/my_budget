from buy.libs.utils import delta_price
from buy.models import Buy
from buy.tests.test_models import Settings


class LibUtilsTest(Settings):
    def test_delta_price(self):
        buy = Buy.objects.all()
        self.assertEqual(0, delta_price(buy))

    def test_delta_price_0(self):
        self.assertEqual(0, delta_price(list()))
