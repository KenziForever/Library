# Generated by Django 5.1.2 on 2024-11-15 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Укажите название товара')),
                ('phone_number', models.IntegerField(verbose_name='Укажите свой номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Укажите почту')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.books')),
            ],
        ),
    ]