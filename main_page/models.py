from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Books(models.Model):
    GENRE_CHOICES = (
        ('Пьеса', 'Пьеса'),
        ('Детектив', 'Детектив'),
        ('Поэма','Поэма'),
        ('Новелла','Новелла'),
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

    def average_rating(self):
        reviews = self.review_films.order_by('created_at')[:5]
        if reviews.exists():
            avg_rating = sum(review.mark for review in reviews) / reviews.count()
            return round(avg_rating, 1)
        return None

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'


class ReviewFilm(models.Model):
    text = models.TextField(null=True)
    review_films = models.ForeignKey(Books, on_delete=models.CASCADE,
                                     related_name='review_films')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзыв о фильме')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_films}-{self.created_at}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'