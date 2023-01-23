# Generated by Django 3.2.16 on 2022-12-19 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_code', models.CharField(max_length=250)),
                ('describtion', models.TextField()),
                ('slug', models.SlugField(max_length=250)),
                ('data_added', models.DateTimeField()),
                ('num_stars', models.IntegerField()),
                ('existence', models.BooleanField()),
                ('num_existence', models.IntegerField()),
                ('Unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('manufacturer', models.CharField(max_length=250)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('review', models.TextField()),
                ('color', models.CharField(max_length=250)),
                ('images', models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/')),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(default='category', related_name='products', to='ShopStore.Category')),
            ],
            options={
                'ordering': ['-data_added'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ShopStore.product')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='categories', to='ShopStore.Product'),
        ),
    ]