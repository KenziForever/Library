# Generated by Django 5.1.2 on 2024-11-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Загрузите картинку:')),
                ('title', models.CharField(max_length=60, verbose_name='Укажите название книги:')),
                ('description', models.TextField(default='Прекрасная книга ', verbose_name='Укажите описание к фильму')),
                ('price', models.FloatField(verbose_name='Укажите цену')),
                ('start_book', models.DateField(verbose_name='Введите дату выхода')),
                ('genre', models.CharField(choices=[('Пьеса', 'Пьеса'), ('Детектив', 'Детектив'), ('Поэма', 'Поэма'), ('Новелла', 'Новелла')], default='Поэма', max_length=70, verbose_name='Укажите жанр')),
                ('mail', models.EmailField(max_length=65, verbose_name='Укажите почту')),
                ('author', models.CharField(max_length=35, verbose_name='Укажите Автора')),
                ('trailer', models.URLField(verbose_name='Укажите ссылку обзора книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]