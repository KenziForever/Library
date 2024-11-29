from django import forms
from .models import Device, Review

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'manufacturer', 'price', 'release_date', 'image', 'category', 'features']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content']
