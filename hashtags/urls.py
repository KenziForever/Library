from django.urls import path
from .views import AllProductsListView, OldListView, NewListView, BabyListView

urlpatterns = [
    path('products/', AllProductsListView.as_view(), name='all_products_list'),
    path('old-products/', OldListView.as_view(), name='Old_tags'),
    path('new-products/', NewListView.as_view(), name='News_tags'),
    path('baby-products/', BabyListView.as_view(), name='Baby_tags'),
]
