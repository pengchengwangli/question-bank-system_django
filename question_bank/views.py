import json
import random
import time

from django.core.files.storage import default_storage
from django.shortcuts import render
from question_bank import models
from django.http import HttpResponse, JsonResponse
# from question_bank import forms
from .models import Question, TestPaper


def danxuan(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
    if request.method != "POST":
        return render(request, 'danxuan.html')
    else:
        return HttpResponse("测试")


def jianda(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
    return render(request, 'jianda.html')


def first(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
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
        "message": "题目保存成功"
    })


def ttff(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
    jsontest = request.body
    jsonn = json.loads(jsontest)
    timu = Question(bank=models.QuestionBank.objects.get(id=1), typename=models.QuestionType.objects.get(id=2),
                    points=models.KnowledgePoints.objects.get(id=1), stem=jsonn['questioncontent'], ans=jsonn['ans'],
                    torf=(
                            jsonn['ans'] == '1'), anss=jsonn['anss'])
    timu.save()
    return JsonResponse({
        "success": True,
        "message": "题目保存成功"
    })


def jd(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
    jsontest = request.body
    jsonn = json.loads(jsontest)
    timu = Question(bank=models.QuestionBank.objects.get(id=1), typename=models.QuestionType.objects.get(id=3),
                    points=models.KnowledgePoints.objects.get(id=1), stem=jsonn['questioncontent'], ans=jsonn['ans'],
                    anss=jsonn['anss'])
    timu.save()
    return JsonResponse({
        "success": True,
        "message": "题目保存成功"
    })


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
    return render(request, 'qbindex.html', context={'user': request.user})


def qblist(request):
    qlist = Question.objects.all()

    return render(request, 'qblist.html', context={'qlist': qlist})


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
        return render(request, 'zuzu.html')


def getk(request):
    loadstr = """{
  "knowledge_points": [
    {
      "id": 1,
      "name": "网络协议"
    },
    {
      "id": 2,
      "name": "网络层次结构"
    },
    {
      "id": 3,
      "name": "数据传输"
    },
    {
      "id": 4,
      "name": "路由算法"
    },
    {
      "id": 5,
      "name": "流量控制"
    }
  ]
}
"""
    tmp = json.loads(loadstr)
    print(tmp)
    return JsonResponse(tmp)


def tf(request):
    if not request.user.is_authenticated:
        return render(request, 'dame.html')
    return render(request, 'tf.html')


def upload_html(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_name = default_storage.save(f'uploads/{time.time()}.html', file)
        file_url = default_storage.url(file_name)
        models.TestPaper.objects.create(url=file_url)
        # tmp.save()
        return JsonResponse({'success': True, 'url': file_url})

    return JsonResponse({'success': False})

def showtest(request):
    testlist = TestPaper.objects.all()
    tlist = []
    for test in testlist:
        tlist.append({"url": test.url})
    return render(request, 'showtest.html',context={'exams': tlist})