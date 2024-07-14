from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from api import views

urlpatterns = [
    path('refresh_captcha/', views.cap, name='captcha'),
    # path('')
]
app_name = 'api'