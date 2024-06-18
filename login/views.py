import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.loader import render_to_string
from django_redis import get_redis_connection
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import random


# Create your views here.
def register(request):
    tips = ""
    if request.method == 'POST':
        print("注册开始")
        # u = request.POST.get('username', '')
        # p = request.POST.get('password', '')
        # e = request.POST.get('email', '')
        # c = request.POST.get('code', '')
        jsonn = json.loads(request.body)
        u = jsonn['username']
        p = jsonn['password']
        e = jsonn['email']
        c = jsonn['code']
        conn = get_redis_connection()
        value = conn.get(e).decode('utf-8')
        print(value)
        # value = value.encode('utf-8')

        if value == c:
            if User.objects.filter(username=u):
                error = {
                    "alert-success": "用户已存在"

                }
                print("用户已存在")

                return JsonResponse(error)
            else:
                user = User.objects.create_user(username=u, email=e, password=p, is_staff=1, is_superuser=1)
                user.save()
                print("注册成功")
                return JsonResponse({"alert-danger": "注册成功"})
        else:
            error = {
                "alert-success": "验证码错误"
            }
            print("验证码错误")
            return JsonResponse(error)

    return render(request, 'register.html')


def sms_code(request):
    code = random.randint(1000, 9999)
    email = request.body
    email_json = json.loads(email)
    email = email_json['email']
    if not email:
        error = {
            "alert-success": "未知错误"
        }
        return JsonResponse(error)
    else:
        conn = get_redis_connection()
        conn.set(email, str(code), ex=120)
        try:
            print(str(code))
            codetemp = render_to_string('getcode.html', context={'code': code})
            send_mail(subject='xxx验证码', message=str(code), from_email="3347132783@qq.com",
                      recipient_list=[email], html_message=codetemp)
        except:
            error = {
                "alert-success": "未知错误"
            }
            return JsonResponse(error)
        return JsonResponse({"alert-danger": "注册成功"})
