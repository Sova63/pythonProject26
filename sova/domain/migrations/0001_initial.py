# Generated by Django 5.0.7 on 2024-12-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=120)),
                ('password', models.TextField()),
                ('user_email', models.CharField(max_length=120)),
            ],
        ),
    ]
