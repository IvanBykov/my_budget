from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-brand', args=[self.id])

    def del_url(self):
        return reverse('del-brand', args=[self.id])


class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-category', args=[self.id])

    def del_url(self):
        return reverse('del-category', args=[self.id])


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-product', args=[self.id])

    def del_url(self):
        return reverse('del-product', args=[self.id])

    def get_plot_price(self):
        return reverse('plot-price', args=[self.id])

    def get_list_price(self):
        return reverse('list-price', args=[self.id])


class Unit(models.Model):
    name = models.CharField(max_length=20)
    name_mini = models.CharField(max_length=5)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('update-unit', args=[self.id])

    def del_url(self):
        return reverse('del-unit', args=[self.id])


class Magazine(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.address}'

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

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.product} - {self.brand} {self.magazine} - {self.date}'

    def get_url(self):
        return reverse('update-buy', args=[self.id])

    def del_url(self):
        return reverse('del-buy', args=[self.id])

    def unit_price(self):
        return self.price / self.amount


class BuyTmp(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(validators=[MinValueValidator(0), ])
    price_unit = models.FloatField(validators=[MinValueValidator(0), ])
    price_buy = models.FloatField(validators=[MinValueValidator(0), ])
    date = models.DateField(null=True, blank=True)
    magazine = models.ForeignKey(Magazine, models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def load_buy(self):
        return reverse('load_buy')
