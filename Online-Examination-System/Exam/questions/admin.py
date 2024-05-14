from django.contrib import admin
from .models import Exam_Model
from .models import*
from .question_models import Question_DB
from .questionpaper_models import Question_Paper
admin.site.register(Question_DB)
admin.site.register(Question_Paper)
#admin.site.register(Special_Students)
admin.site.register(Exam_Model)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Subject)
