# Generated by Django 4.0.4 on 2022-05-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_category_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]