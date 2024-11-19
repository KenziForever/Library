from django.shortcuts import render
from . import models

def all_products_list_view(request):
    if request.method == 'GET':
        products_list = models.Product.objects.filter().order_by('-id')
        context = {'products_list': products_list}
        return render(request, 'all_products_list_view.html',
                      context=context)

def old_list_view(request):
    if request.method == 'GET':
        Old = models.Product.objects.filter(tags__name="Для старых").order_by('-id')
        context = {'Old': Old}
        return render(request, 'Old.html',
                      context=context)

def new_list_view(request):
    if request.method == 'GET':
        News = models.Product.objects.filter(tags__name="Для молодых").order_by('-id')
        context = {'News': News}
        return render(request, 'News.html',
                      context=context)

def baby_list_view(request):
    if request.method == 'GET':
        Baby = models.Product.objects.filter(tags__name="Для детей").order_by('-id')
        context = {'Baby': Baby}
        return render(request, 'Baby.html',
                      context=context)