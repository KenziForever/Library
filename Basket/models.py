from django.db import models
from main_page.models import Books


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Укажите имя")
    phone_number = models.IntegerField(verbose_name="Укажите свой номер телефона")
    email = models.EmailField(verbose_name="Укажите почту")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Заказ от {self.name} на {self.book}"
