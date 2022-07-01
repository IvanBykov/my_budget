from django.test import TestCase
from django.core.exceptions import ValidationError

from buy.models import Brand, Category, Product


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


class BrandModelTest(Settings):
    def test_validators_value(self):
        print('----------------brand------------------')
        print(self.brand.name)
        self.assertEqual('бренд', self.brand.name)
        print(self.brand._meta.get_field('name').validators[0].limit_value)
        self.assertEqual(40, self.brand._meta.get_field('name').max_length)

    def test_validator_fail(self):
        brand_invalid = Brand(name='g'*41)
        with self.assertRaises(ValidationError):
            brand_invalid.full_clean()
            brand_invalid.save()


class CategoryModelTest(Settings):
    def test_validators_value(self):
        self.assertEqual('категория', self.category.name)
        self.assertEqual(60, self.category._meta.get_field('name').max_length)

    def test_validator_fail(self):
        s1 = 'ы'*61
        category_invalid = Category(name=s1)
        with self.assertRaises(ValidationError):
            category_invalid.full_clean()
            category_invalid.save()


class ProductModelTest(Settings):
    def test_validator_value(self):
        self.assertEqual('продукт', self.product.name)
        self.assertEqual(100, self.product._meta.get_field('name').max_length)
        print(self.product._meta.get_field('category'))

    def test_validater_fail(self):
        product_invalid = Product(
            name='a'*101)
        with self.assertRaises(ValidationError):
            product_invalid.full_clean()
            product_invalid.save()
