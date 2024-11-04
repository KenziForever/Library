from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('About_me/', views.about_me, name="about_me"),
    path('My_pets/', views.about_my_pets, name='My_pets'),
    path('Time/', views.system_time, name='Time'),
]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)