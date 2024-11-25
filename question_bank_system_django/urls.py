"""question_bank_system_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render
from . import views as index
from temp_ import views
from django.http import HttpResponseRedirect

urlpatterns = [
                  path('', index.index),
                  path('index/', lambda request: render(request, 'index.html', context={'user': request.user}),
                       name='index'),
                  path('admin/', admin.site.urls),
                  path('login/', include('login.urls', namespace='login')),
                  path('temp/', views.temp, name='tmp'),
                  path('captcha/', include('captcha.urls')),
                  path('api/', include('api.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('test/', index.test),
                  path('qb/', include('question_bank.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 媒体路由地址
