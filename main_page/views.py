from urllib import request
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def books_list_view(request):
    if request.method == 'GET':
        book_list = models.Books.objects.all()
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)

def books_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('🙂Меня зовут Аймир мне 14 лет👌'
                            'учусь в 66 школе, люблю играть '
                            'неплохо учусь много друзей🤗')

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse('🙂В данный момент нет питомца '
                            'раньше была собакa породы "Алабай"'
                            'люблю кошек, собак и хомячков😶‍🌫️')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(f'В данный момент время {datetime.now()}👍👍👍')

