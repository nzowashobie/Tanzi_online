from django.urls import path
from . import views
urlpatterns = [
    
    path('select-grade/', views.select_grade, name='select_grade'),
    path('grade/<str:grade_id>/', views.grade_subjects, name='grade_subjects'),
    path('grade/<str:grade_id>/<str:subject_id>/', views.assign_test_to_students, name='success_page'),    
    path('prof/viewexams/',views.view_exams_prof,name="view_exams"),
    path('prof/viewpreviousexams/',views.view_previousexams_prof,name="faculty-previous"),
    path('prof/viewresults/',views.view_results_prof,name="faculty-result"),
    path('prof/addquestions/',views.add_questions,name="faculty-addquestions"),
    path('prof/addnewquestionpaper/',views.add_question_paper,name="faculty-add_question_paper"),
    #path('prof/<teacher_id>/exam/<test_id>/students/',views.view_students_prof,name="faculty-student"),
    path('prof/viewstudents/',views.view_students_prof,name="faculty-student"),
    path('student/viewexams/',views.view_exams_student,name="view_exams_student"),
    path('student/previous/',views.student_view_previous,name="student-previous"),
    path('student/appear/<int:id>',views.appear_exam,name = "appear-exam"),
    path('student/result/<int:id>',views.result,name = "result"),
    path('student/attendance/',views.view_students_attendance,name="view_students_attendance")
]