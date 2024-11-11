from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Пьеса', 'Пьеса'),
        ('Детектив', 'Детектив'),
        ('Поэма','Поэма'),
        ('Новелла','Новелла')
    )
    image = models.ImageField(upload_to = 'books/', verbose_name = 'Загрузите картинку:')
    title = models.CharField(max_length=60, verbose_name='Укажите название книги:')
    description = models.TextField(verbose_name='Укажите описание к фильму', default='Прекрасная книга ')
    price = models.FloatField(verbose_name='Укажите цену')
    start_book = models.DateField(verbose_name='Введите дату выхода')
    genre = models.CharField(max_length=70, choices=GENRE_CHOICES, default='Поэма', verbose_name='Укажите жанр')
    mail = models.EmailField(max_length=65, verbose_name='Укажите почту')
    author = models.CharField(max_length=35, verbose_name='Укажите Автора')
    trailer = models.URLField(verbose_name='Укажите ссылку обзора книги')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'
