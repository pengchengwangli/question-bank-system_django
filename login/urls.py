from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('register/', views.register, name='reg')
]
app_name = 'login'
