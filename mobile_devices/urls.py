from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='device_list'),
    path('device/<int:pk>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device/add/', views.DeviceCreateView.as_view(), name='add_device'),
    path('device/edit/<int:pk>/', views.DeviceUpdateView.as_view(), name='edit_device'),
    path('device/delete/<int:pk>/', views.DeviceDeleteView.as_view(), name='delete_device'),
]
