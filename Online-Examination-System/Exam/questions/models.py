from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField

from .questionpaper_models import Question_Paper

from django import forms

class Grade(models.Model):
    grade_name = models.CharField(max_length=50,blank=True)
    
    
    def __str__(self):
        return self.grade_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.subject_name
   
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True)
    subject = models.ManyToManyField(Subject,  blank=True)
   # def __str__(self):
    #    return self.user

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Exam_Model(models.Model):
    #professor = models.CharField(max_length=50, blank=True) 
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, blank=True, null=True)
    total_marks = models.IntegerField()
    question_paper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, related_name='exams')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True)
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class ExamForm(ModelForm):
   
    def __init__(self,professor,*args,**kwargs):
        super (ExamForm,self ).__init__(*args,**kwargs) 
        self.fields['question_paper'].queryset = Question_Paper.objects.filter(professor=professor)


    class Meta:
        model = Exam_Model
        fields = '__all__'
        exclude = ['professor','students']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'total_marks' : forms.NumberInput(attrs = {'class':'form-control'}),
            'start_time': forms.DateTimeInput(attrs = {'class':'form-control'}),
            'end_time': forms.DateTimeInput(attrs = {'class':'form-control'})
        }
        labels = {
            'name': 'Test Name',
        }