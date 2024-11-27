from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.views import generic
from . import models
from .forms import CommentForm
from django.views import View
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class BookListView(generic.ListView):
    template_name = "book.html"
    context_object_name = "books"
    model = models.Books

    def get_queryset(self):
        return models.Books.objects.all()


class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"
    model = models.Books
    context_object_name = "book_id"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.object
            comment.save()
            return redirect(
                "book-detail", pk=self.object.pk
            )  # Редирект на ту же страницу
        return self.get(request, *args, **kwargs)


class AboutMeView(View):
    def get(self, request):
        return HttpResponse(
            "🙂Меня зовут Аймир мне 14 лет👌"
            "учусь в 66 школе, люблю играть "
            "неплохо учусь много друзей🤗"
        )


class AboutMyPetsView(View):
    def get(self, request):
        return HttpResponse(
            "🙂В данный момент нет питомца "
            'раньше была собакa породы "Алабай"'
            "люблю кошек, собак и хомячков😶‍🌫️"
        )


class SystemTimeView(View):
    def get(self, request):
        return HttpResponse(f"В данный момент время {datetime.now()}👍👍👍")
