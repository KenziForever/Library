from django.shortcuts import render
from django.views import View
from . import models

class AllProductsListView(View):
    def get(self, request):
        products_list = models.Product.objects.filter().order_by('-id')
        context = {'products_list': products_list}
        return render(request, 'all_products_list_view.html', context=context)

class OldListView(View):
    def get(self, request):
        Old = models.Product.objects.filter(tags__name="Для старых").order_by('-id')
        context = {'Old': Old}
        return render(request, 'Old.html', context=context)

class NewListView(View):
    def get(self, request):
        News = models.Product.objects.filter(tags__name="Для молодых").order_by('-id')
        context = {'News': News}
        return render(request, 'News.html', context=context)

class BabyListView(View):
    def get(self, request):
        Baby = models.Product.objects.filter(tags__name="Для детей").order_by('-id')
        context = {'Baby': Baby}
        return render(request, 'Baby.html', context=context)
