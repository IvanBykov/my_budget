from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)


class Unit(models.Model):
    name = models.CharField(max_length=20)
    name_mini = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Magazine(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    date = models.DateField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    magazine = models.ForeignKey(Magazine, models.PROTECT)
