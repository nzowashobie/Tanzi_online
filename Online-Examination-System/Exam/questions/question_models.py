from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from django import forms
from ckeditor_uploader.fields import RichTextUploadingField 

class Question_DB(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE, null=True)
    qno = models.AutoField(primary_key=True)
    question = RichTextUploadingField(config_name='extends')
    optionA = RichTextUploadingField(config_name='extends')
    optionB = RichTextUploadingField(config_name='extends')
    optionC = RichTextUploadingField(config_name='extends')
    optionD = RichTextUploadingField(config_name='extends')
    answer = RichTextUploadingField(config_name='extends')
    max_marks = models.IntegerField(default=0)

    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '
class QForm(ModelForm):
    class Meta:
        model = Question_DB
        fields = '__all__'
        exclude = ['qno', 'professor']
        widgets = {
            'question': forms.TextInput(attrs = {'class':'form-control'}),
            'optionA': forms.TextInput(attrs = {'class':'form-control'}),
            'optionB': forms.TextInput(attrs = {'class':'form-control'}),
            'optionC': forms.TextInput(attrs = {'class':'form-control'}),
            'optionD': forms.TextInput(attrs = {'class':'form-control'}),
            'answer': forms.TextInput(attrs = {'class':'form-control'}),
            'max_marks': forms.NumberInput(attrs = {'class':'form-control'}),
        }