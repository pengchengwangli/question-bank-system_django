from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('register/', views.register, name='reg'),
    path('smsemail/',views.sms_code,name='code'),
]
app_name = 'login'
