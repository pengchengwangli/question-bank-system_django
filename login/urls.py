from django.urls import path, re_path, include
# from django.conf.urls.static import static
from django.shortcuts import redirect
# from django.conf import settings

from . import views

urlpatterns = [
    path('register/', views.register, name='reg'),
    path('smsemail/', views.sms_code, name='code'),
    path('login/', views.login_, name='login'),
    path('out/',views.outlogin,name='out'),
    path('repass/',views.repass,name='repass'),
    path('verify_code/',views.verify_code,name="verify_code"),
    path('',lambda request:redirect('login:login')),
    # path('captcha/', include('captcha.urls')),
    # path('getcode/',views.getcode,name='getcode'),
]
app_name = 'login'
