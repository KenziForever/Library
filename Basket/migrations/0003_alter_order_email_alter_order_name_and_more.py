# Generated by Django 5.1.2 on 2024-11-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Basket", "0002_alter_order_book_alter_order_email_alter_order_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Укажите почту"),
        ),
        migrations.AlterField(
            model_name="order",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Укажите имя"),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone_number",
            field=models.IntegerField(verbose_name="Укажите свой номер телефона"),
        ),
    ]
