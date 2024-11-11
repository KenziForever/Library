from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list_view, name='books'),
    path('book_detail/<int:id>/', views.books_view, name='detail'),
]
