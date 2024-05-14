
from django import forms
from .models import Exam_Model, Student
from .models import Grade, Subject
from .models import Grade


class GradeForm(forms.Form):
    grade = forms.ModelChoiceField(queryset=Grade.objects.all())
   
class TestAssignmentForm(forms.Form):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.none(), widget=forms.CheckboxSelectMultiple)
   
    def __init__(self, *args, grade=None, subject=None, **kwargs):
        super(TestAssignmentForm, self).__init__(*args, **kwargs)
        
        if grade is not None and subject is not None:
            # Filter students based on grade and subject
            #self.fields['students'] = forms.ModelMultipleChoiceField(queryset=Exam_Model.objects.filter(grade=grade, subject=subject),  widget=forms.CheckboxSelectMultiple)
            self.fields['students'] = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(grade=grade, subject=subject),  widget=forms.CheckboxSelectMultiple)

# forms.py

class SubjectGradeForm(forms.Form):
    grade = forms.ModelChoiceField(queryset=Grade.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    


