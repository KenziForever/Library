from django.urls import path
from .views import BookListView, BookDetailView, AboutMeView, AboutMyPetsView, SystemTimeView

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about_me'),
    path('about-my-pets/', AboutMyPetsView.as_view(), name='about_my_pets'),
    path('system-time/', SystemTimeView.as_view(), name='system_time'),
    path('', BookListView.as_view(), name='books_list_view'),
    path('book_detail/<int:id>/', BookDetailView.as_view(), name='book_detail'),
]
