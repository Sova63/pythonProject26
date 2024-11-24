# Generated by Django 5.1.1 on 2024-09-28 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=40)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('pages', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intshop.category_product')),
            ],
        ),
    ]
