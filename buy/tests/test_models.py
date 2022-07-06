from django.test import TestCase
from django.core.exceptions import ValidationError

from buy.models import Brand, Category, Product, Unit, Magazine, Buy


class Settings(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.brand = Brand.objects.create(name='бренд')
        cls.category = Category.objects.create(name='категория')
        cls.product = Product.objects.create(
            name='продукт',
            category=cls.category
        )
        cls.unit = Unit.objects.create(
            name='метр',
            name_mini='м'
        )
        cls.magazine = Magazine.objects.create(
            name='Магнит',
            address='адрес'
        )
        cls.buy = Buy.objects.create(
            product=cls.product,
            amount=2,
            date='2022-06-12',
            unit=cls.unit,
            magazine=cls.magazine,
            price=15,
            brand=cls.brand
        )


class BrandModelTest(Settings):
    def test_validators_value(self):
        self.assertEqual('бренд', self.brand.name)
        self.assertEqual(40, self.brand._meta.get_field('name').max_length)

    def test_validator_fail(self):
        brand_invalid = Brand(name='g' * 41)
        with self.assertRaises(ValidationError):
            brand_invalid.full_clean()
            brand_invalid.save()


class CategoryModelTest(Settings):
    def test_validators_value(self):
        self.assertEqual('категория', self.category.name)
        self.assertEqual(60, self.category._meta.get_field('name').max_length)

    def test_validator_fail(self):
        s1 = 'ы' * 61
        category_invalid = Category(name=s1)
        with self.assertRaises(ValidationError):
            category_invalid.full_clean()
            category_invalid.save()


class ProductModelTest(Settings):
    def test_validator_value(self):
        self.assertEqual('продукт', self.product.name)
        self.assertEqual(100, self.product._meta.get_field('name').max_length)
        # print(self.product._meta.get_field('category').validators[0].limit_value)

    def test_validater_fail(self):
        product_invalid = Product(
            name='a' * 101)
        with self.assertRaises(ValidationError):
            product_invalid.full_clean()
            product_invalid.save()


class UnitModelTest(Settings):
    def test_validator_value(self):
        self.assertEqual('метр', self.unit.name)
        self.assertEqual(20, self.unit._meta.get_field('name').max_length)
        self.assertEqual('м', self.unit.name_mini)
        self.assertEqual(5, self.unit._meta.get_field('name_mini').max_length)

    def test_validater_fail(self):
        unit_invalid = Unit(name='f' * 21, name_mini='s')
        with self.assertRaises(ValidationError):
            unit_invalid.full_clean()
            unit_invalid.save()
        unit_invalid = Unit(name='d' * 21, name_mini='f' * 5)
        with self.assertRaises(ValidationError):
            unit_invalid.full_clean()
            unit_invalid.save()


class MagazineModelTest(Settings):
    def test_validator_value(self):
        self.assertEqual('Магнит', self.magazine.name)
        self.assertEqual(50, self.magazine._meta.get_field('name').max_length)
        self.assertEqual('адрес', self.magazine.address)
        self.assertEqual(100, self.magazine._meta.get_field('address').max_length)

    def test_validator_fail(self):
        magazine_invalid = Magazine(name='d' * 51)
        with self.assertRaises(ValidationError):
            magazine_invalid.full_clean()
            magazine_invalid.save()
        magazine_invalid = Magazine(name='d' * 20, address='w' * 101)
        with self.assertRaises(ValidationError):
            magazine_invalid.full_clean()
            magazine_invalid.save()


class BuyModelTest(Settings):
    def test_validator_value(self):
        self.assertEqual('продукт', self.buy.product.name)
        self.assertEqual(2, self.buy.amount)
        self.assertEqual('2022-06-12', self.buy.date)
        self.assertEqual('метр', self.buy.unit.name)
        self.assertEqual('Магнит', self.buy.magazine.name)
        self.assertEqual(15, self.buy.price)
        self.assertEqual('бренд', self.buy.brand.name)
        # self.assertEqual(1, self.buy._meta.get_field('amount').validators[0].min_value)
        # print(self.buy._meta.get_field('amount'))

    def test_validator_fail(self):
        buy_invalid = Buy(amount=-1, date='2022-06-12', magazine=self.magazine, product=self.product, unit=self.unit,
                          price=10)
        with self.assertRaises(ValidationError):
            buy_invalid.full_clean()
            buy_invalid.save()
        buy_invalid.amount = 1
        buy_invalid.price = -1
        with self.assertRaises(ValidationError):
            buy_invalid.full_clean()
            buy_invalid.save()

    def test_get_price(self):
        self.assertEqual(7.5, self.buy.unit_price())
        #print(self.buy.get_url(self))
