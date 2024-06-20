from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from api import views

urlpatterns = [
    path('refresh_captcha/', views.cap, name='captcha'),
]
app_name = 'api'