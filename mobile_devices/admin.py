from django.contrib import admin
from .models import Device, Category, Feature, Review

admin.site.register(Device)
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(Review)
