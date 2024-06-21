from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.shortcuts import render
from captcha.fields import CaptchaField
from django.forms import forms
# Create your views here.
class capF(forms.Form):
    captcha_ = CaptchaField()
def temp(request):
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    return render(request,'tmp1.html',context={'hashkey':hashkey,'image_url':image_url})


# def index(request):
#     return None