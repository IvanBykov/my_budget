from django.contrib import admin
from .models import Product, Unit, Magazine, Brand, Category, Buy
# Register your models here.

admin.site.register(Product)
admin.site.register(Unit)
admin.site.register(Magazine)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Buy)
