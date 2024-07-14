from ckeditor.fields import RichTextField
from django.db import models

# class QAmodel(models.Model):
# from django.db import models
# # 不带图片上传
# from ckeditor.fields import RichTextField
# # 带图片上传
# from ckeditor_uploader.fields import RichTextUploadingField
#
#
# # Create your models here.
# class MyNote(models.Model):
#     title = models.CharField(max_length=64, default='a default title')
#     content = RichTextUploadingField(config_name='default')
# #     content = RichTextField(verbose_name='正文内容',config_name='default')  # config_name指定ckeditor配置文件，不指定就使用default
