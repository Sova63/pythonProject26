# Generated by Django 5.1.3 on 2024-11-28 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='name',
        ),
    ]
