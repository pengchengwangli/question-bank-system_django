from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def cap(request):
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    return JsonResponse({'hashkey': hashkey, 'image_url': image_url})
