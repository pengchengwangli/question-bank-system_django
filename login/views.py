import base64
import json

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import QuerySet
from django.shortcuts import render
from django.template.loader import render_to_string
from django_redis import get_redis_connection
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
# from django.conf import settings
# import captcha
# from utils.codeget import check_code
from django.http import FileResponse
from django.shortcuts import redirect
from captcha.models import CaptchaStore
import random


# Create your views here.
def register(request):
    if request.method == 'POST':
        print("注册开始")
        jsonn = json.loads(request.body)
        u = jsonn['username']
        p = jsonn['password']
        e = jsonn['email']
        c = jsonn['code']
        cap: str = jsonn['captcha']
        hashkey = jsonn['hashkey']
        # print(cap)
        code: QuerySet = CaptchaStore.objects.filter(hashkey=hashkey)
        # print(code[0].response)
        if (code.count() == 0) or code[0].response != cap.lower():
            # print(code, code[0].response)
            # print(code.count())
            # print(code[0].response,cap)
            return JsonResponse({"success": False,
                                 "message": "图片验证码错误!"})
        conn = get_redis_connection()
        value = conn.get(e)
        if value:
            value = value.decode('utf-8')
        # print(value)
        # value = value.encode('utf-8')

        if value == c:
            if User.objects.filter(email=e):
                error = {
                    "success": False,
                    "message": "邮箱已存在!"
                }
                return JsonResponse(error)
            if User.objects.filter(username=u):
                error = {
                    "success": False,
                    "message": "用户已存在!"
                }
                print("用户已存在")

                return JsonResponse(error)
            else:
                user = User.objects.create_user(username=u, email=e, password=p, is_staff=1, is_superuser=1)
                user.save()
                id = User.objects.get(username=u).id
                print("注册成功")
                return JsonResponse({
                    "success": True,
                    "message": "注册成功",
                    "user": {
                        "id": id,
                        "username": u,
                        "email": e
                    }
                }
                )
        else:
            error = {
                "success": False,
                "message": "验证码错误!"
            }
            print("验证码错误")
            return JsonResponse(error)
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    return render(request, 'register.html', {'hashkey': hashkey, 'image_url': image_url})


def login_(request):
    if request.method == 'POST':

        json_text = request.body
        json_dic = json.loads(json_text)
        imgcode = json_dic['captcha']
        hashkey = json_dic['hashkey']
        _code = CaptchaStore.objects.filter(hashkey=hashkey)
        print(_code)
        print(imgcode)
        if len(_code) == 0 or _code[0].response.lower() != imgcode.lower():
            mess = {
                "success": False,
                "message": "图片验证码错误"
            }
            return JsonResponse(mess)
        u = json_dic['username']
        p = json_dic['password']
        if User.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    login(request, user)
                mess = {
                    "success": True,
                    "message": "登录成功正在跳转"
                }
                return JsonResponse(mess)
            else:
                error = {
                    "success": False,
                    "message": "用户名或密码错误"
                }
                return JsonResponse(error)
        else:
            error = {
                "success": False,
                "message": "用户名或密码错误"
            }
            return JsonResponse(error)
    else:
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        return render(request, 'login.html', {"image_url": image_url, 'hash_key': hashkey})


def outlogin(request):
    logout(request)
    return redirect('index')


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
                "success": False,
                "message": "发送验证码失败，请稍后再试"
            }
            return JsonResponse(error)
        return JsonResponse({
            "success": True,
            "message": "验证码已发送到您的邮箱"
        }
        )


def repass(request):
    return render(request, 'repassword.html')


def verify_code(request):
    if request.method == "POST":
        json_dic = json.loads(request.body)
        email = json_dic['email']
        code = json_dic['code']
        passwd = json_dic['password']
        user = User.objects.filter(email=email)
        conn = get_redis_connection()
        _code = conn.get(email)
        if (not user.count()) or (not _code) or code != _code.decode('utf-8'):
            error = {
                "success": False,
                "message": "验证码错误"
            }
            return JsonResponse(error)
        else:
            user_ = User.objects.get(email=email)
            user_.set_password(passwd)
            user_.save()
            # user[0].set_password(passwd)
            # user[0].save()
            return JsonResponse({
                "success": True,
                "message": "密码修改成功!"
            })
