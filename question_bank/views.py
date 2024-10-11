import json
import random

from django.shortcuts import render
from question_bank import models
from django.http import HttpResponse, JsonResponse
# from question_bank import forms
from .models import Question


def danxuan(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    if request.method != "POST":
        return render(request, 'danxuan.html')
    else:
        return HttpResponse("测试")

def jianda(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    return render(request,'jianda.html')


def first(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    jsontest = request.body
    # print(jsontest)
    jsonn = json.loads(jsontest)
    print(jsonn)
    # 向数据库中插入

    timu = Question(bank=models.QuestionBank.objects.get(id=1), typename=models.QuestionType.objects.get(id=1),
                    points=models.KnowledgePoints.objects.get(id=1), stem=jsonn['questionContent'],
                    option=jsonn['options'], ans=jsonn['ans'], anss=jsonn['anss'])
    timu.save()
    return JsonResponse({
        "success": True,
        "message": "xxxxxxx保存成功"
    })

def ttff(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    jsontest = request.body
    jsonn = json.loads(jsontest)
    timu = Question(bank=models.QuestionBank.objects.get(id=1), typename=models.QuestionType.objects.get(id=2),
                    points=models.KnowledgePoints.objects.get(id=1), stem=jsonn['questioncontent'], ans=jsonn['ans'],torf=(
                    jsonn['ans'] == '1'), anss=jsonn['anss'])
    timu.save()
    return JsonResponse({
        "success": True,
        "message": "xxxxxxx保存成功"
    })
def jd(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    jsontest = request.body
    jsonn = json.loads(jsontest)
    timu = Question(bank=models.QuestionBank.objects.get(id=1), typename=models.QuestionType.objects.get(id=3),
                    points=models.KnowledgePoints.objects.get(id=1), stem=jsonn['questioncontent'], ans=jsonn['ans'],anss=jsonn['anss'])
    timu.save()
    return JsonResponse({
        "success": True,
        "message": "xxxxxxx保存成功"
    })

def index(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    return render(request, 'qbindex.html',context={'user':request.user})

def qblist(request):
    qlist = Question.objects.all()

    return render(request,'qblist.html',context={'qlist':qlist})
def zuzu(request):

    if request.method == 'POST':
        bodystr = request.body
        loadstr = json.loads(bodystr)
        mcq_count = loadstr['mcq_count']
        tf_count = loadstr['tf_count']
        sa_count = loadstr['sa_count']
        returnstr = ''
        count = Question.objects.filter(typename=1).count()
        random_offsets = random.sample(range(count), min(count, mcq_count))
        random_questions = [Question.objects.filter(typename=1).all()[offset] for offset in random_offsets]
        for qset in random_questions:
            returnstr += qset.stem
        count = Question.objects.filter(typename=2).count()
        random_offsets = random.sample(range(count), min(count, tf_count))
        random_questions = [Question.objects.filter(typename=2).all()[offset] for offset in random_offsets]
        for qset in random_questions:
            returnstr += qset.stem
        count = Question.objects.filter(typename=3).count()
        random_offsets = random.sample(range(count), min(count, sa_count))
        random_questions = [Question.objects.filter(typename=3).all()[offset] for offset in random_offsets]
        for qset in random_questions:
            returnstr += qset.stem
        # print(random_questions[0].stem)
        return HttpResponse(returnstr)
    else:
        return render(request,'zuzu.html')

def tf(request):
    if not request.user.is_authenticated:
        return render(request,'dame.html')
    return render(request, 'tf.html')
