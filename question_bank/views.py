import json

from django.shortcuts import render
from question_bank import models
from django.http import HttpResponse , JsonResponse
# from question_bank import forms
from .models import Question
def danxuan(request):

    if request.method!= "POST":
        return render(request, 'danxuan.html' )
    else:

        return HttpResponse("测试")
def first(request):
    jsontest = request.body
    # print(jsontest)
    jsonn = json.loads(jsontest)
    print(jsonn)
    timu = Question(bank=models.QuestionBank.objects.get(id=1),typename=models.QuestionType.objects.get(id=1),points=models.KnowledgePoints.objects.get(id=1),stem=jsonn['questionContent'],option=jsonn['options'],ans=jsonn['ans'],anss=jsonn['anss'])
    timu.save()
    return JsonResponse({
                    "success": True,
                    "message": "xxxxxxx保存成功"
})



