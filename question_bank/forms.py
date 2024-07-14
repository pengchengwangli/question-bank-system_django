from question_bank import models
from django import forms
from .models import Question

# from ckeditor.widgets import CKEditorWidget


class QForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


