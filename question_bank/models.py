from django.db import models
from django.contrib.auth import models as authmodels


# Create your models here.

class QuestionBank(models.Model):
    qkname = models.CharField(verbose_name="题库名", max_length=120)
    creator = models.ForeignKey(verbose_name="创建人", to=authmodels.User, on_delete=models.CASCADE)
    creationdate = models.DateField(verbose_name="修改日期", auto_now=True, null=False)


class QuestionType(models.Model):
    typename = models.CharField(verbose_name="题型名", max_length=120)


class KnowledgePoints(models.Model):
    pointsname = models.CharField(verbose_name="知识点名", max_length=120)
    qbname = models.ForeignKey(verbose_name="题库", to=QuestionBank, on_delete=models.CASCADE)


class Question(models.Model):
    bank = models.ForeignKey(verbose_name="所属题库",to=QuestionBank,on_delete=models.CASCADE)
    typename = models.ForeignKey(verbose_name="题型",to=QuestionType,on_delete=models.CASCADE)
    points = models.ForeignKey(verbose_name="知识点",to=KnowledgePoints,on_delete=models.SET_NULL)
    stem = models.TextField(verbose_name="题干")
    torf = models.BooleanField(verbose_name="判断的对错",default=True)
    option = models.JSONField(verbose_name="选项")
    ans = models.TextField(verbose_name="答案")
    anss = models.TextField(verbose_name="解析")

