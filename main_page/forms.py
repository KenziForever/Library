from .models import ReviewFilm
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = ReviewFilm
        fields = ["text"]
