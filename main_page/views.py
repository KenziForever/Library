from urllib import request
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


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

