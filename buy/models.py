from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-brand', args=[self.id])


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-category', args=[self.id])


class Product(models.Model):
    name = models.CharField(max_length=100)
    # brand = models.ForeignKey(Brand, models.PROTECT, null=True, blank=True)
    category = models.ForeignKey(Category, models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-product', args=[self.id])


class Unit(models.Model):
    name = models.CharField(max_length=20)
    name_mini = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-unit', args=[self.id])


class Magazine(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-magazine', args=[self.id])

    def del_url(self):
        return reverse('del-magazine', args=[self.id])


class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.FloatField(validators=[MinValueValidator(0), ])
    date = models.DateField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    magazine = models.ForeignKey(Magazine, models.PROTECT)
    price = models.FloatField(validators=[MinValueValidator(0), ])
    brand = models.ForeignKey(Brand, models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.product} - { self.brand } {self.magazine} - {self.date}'

    def get_url(self):
        return reverse('update-buy', args=[self.id])
