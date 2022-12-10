# Generated by Django 3.2.16 on 2022-12-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopStore', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(default='category', related_name='products', to='ShopStore.Category'),
        ),
    ]
