from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list_view, name='books_list_view'),
    path('book_detail/<int:id>/', views.books_view, name='book_detail'),
]
