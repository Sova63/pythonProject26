# Generated by Django 5.0.7 on 2024-12-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_rename_user_id_entry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='username',
            field=models.CharField(max_length=120),
        ),
    ]