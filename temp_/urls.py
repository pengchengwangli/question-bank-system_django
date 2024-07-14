from django.urls import path, re_path, include
# from django.conf.urls.static import static
from django.shortcuts import redirect
from temp_ import views
# from django.conf import settings

urlpatterns = [
    path('temp/',views.cktest)
]
app_name = "temp_"