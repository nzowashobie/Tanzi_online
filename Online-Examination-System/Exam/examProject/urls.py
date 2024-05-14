"""examProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings

from questions.views import assign_test_to_students, grade_subjects, select_grade
from . import views
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('exams/prof/viewexams/select-grade/', select_grade, name='select_grade'),
    path('grade/<str:grade_id>/', grade_subjects, name='grade_subjects'),
    path('grade/<str:grade_id>/<str:subject_id>/', assign_test_to_students, name='success_page'),    
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('faculty/',include('faculty.urls')),
    path('student-pref/',include('studentPreferences.urls')),
    path('exams/',include('questions.urls')),
    path('',views.index,name = "homepage"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)