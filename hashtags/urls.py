from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products_list_view, name='all_products_tags'),
    path('Old_products/', views.old_list_view, name='Old_tags'),
    path('News_products/', views.new_list_view, name='News_tags'),
    path('Baby_products/', views.baby_list_view, name='Baby_tags'),

]