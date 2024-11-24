# Generated by Django 5.1.1 on 2024-09-16 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_product',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=40)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intshop.category_product')),
            ],
        ),
    ]