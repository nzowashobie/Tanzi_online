from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from faculty.models import FacultyInfo
import questions
#from .models import Answer, Grade, Question, Student, Subject, Test
from questions.forms import GradeForm, TestAssignmentForm
from .models import *
from django.contrib.auth.models import Group
from student.models import *
from django.utils import timezone
from student.models import StuExam_DB,StuResults_DB
from questions.questionpaper_models import QPForm
from questions.question_models import QForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

@login_required(login_url='faculty-login')
def view_exams_prof(request):
    prof = request.user
    prof_user = User.objects.get(username=prof)
    permissions = False
    if prof:
        permissions = has_group(prof,"Professor")
    if permissions:
        new_Form = ExamForm(prof_user)
        if request.method == 'POST' and permissions:
            form = ExamForm(prof_user,request.POST)
            if form.is_valid():
                exam = form.save(commit=False)
                exam.professor = prof
                exam.save()
                
                return redirect('select_grade')

        exams = Exam_Model.objects.filter(professor=prof)
        return render(request, 'exam/mainexam.html', {
            'exams': exams, 'examform': new_Form, 'prof': prof,
        })
    else:
        return redirect('view_exams_student')

@login_required(login_url='faculty-login')
def add_question_paper(request):
    prof = request.user
    prof_user = User.objects.get(username=prof)
    permissions = False
    if prof:
        permissions = has_group(prof,"Professor")
    if permissions:
        new_Form = QPForm(prof_user)
        if request.method == 'POST' and permissions:
            form = QPForm(prof_user,request.POST)
            if form.is_valid():
                exam = form.save(commit=False)
                exam.professor = prof_user
                exam.save()
                form.save_m2m()
                return redirect('faculty-add_question_paper')

        exams = Exam_Model.objects.filter(professor=prof)
        return render(request, 'exam/addquestionpaper.html', {
            'exams': exams, 'examform': new_Form, 'prof': prof,
        })
    else:
        return redirect('view_exams_student')

@login_required(login_url='faculty-login')
def add_questions(request):
    prof = request.user
    prof_user = User.objects.get(username=prof)
    permissions = False
    if prof:
        permissions = has_group(prof,"Professor")
    if permissions:
        new_Form = QForm()
        if request.method == 'POST' and permissions:
            form = QForm(request.POST)
            if form.is_valid():
                exam = form.save(commit=False)
                exam.professor = prof_user
                exam.save()
                form.save_m2m()
                return redirect('faculty-addquestions')

        exams = Exam_Model.objects.filter(professor=prof)
        return render(request, 'exam/addquestions.html', {
            'exams': exams, 'examform': new_Form, 'prof': prof,
        })
    else:
        return redirect('view_exams_student')

@login_required(login_url='faculty-login')
def view_previousexams_prof(request):
    prof = request.user
    student = 0
    exams = Exam_Model.objects.filter(professor=prof)
    return render(request, 'exam/previousexam.html', {
        'exams': exams,'prof': prof
    })

@login_required(login_url='login')
def student_view_previous(request):
    exams = Exam_Model.objects.all()
    list_of_completed = []
    list_un = []
    for exam in exams:
        if StuExam_DB.objects.filter(examname=exam.name ,student=request.user).exists():
            if StuExam_DB.objects.get(examname=exam.name,student=request.user).completed == 1:
                list_of_completed.append(exam)
        else:
            list_un.append(exam)

    return render(request,'exam/previousstudent.html',{
        'exams':list_un,
        'completed':list_of_completed
    })

@login_required(login_url='faculty-login')
def view_students_prof(request):
    students = User.objects.filter(groups__name = "Student")
    # students = User.objects.filter(groups__name = "Student")
    
    student_name = []
    student_completed = []
    count = 0
    dicts = {}
    examn = Exam_Model.objects.filter(professor=request.user)
    for student in students:
        student_name.append(student.first_name + " " + student.last_name )
        count = 0
        for exam in examn:
            if StuExam_DB.objects.filter(student=student,examname=exam.name,completed=1).exists():
                count += 1
            else:
                count += 0
        student_completed.append(count)
    i = 0
    for x in student_name:
        dicts[x] = student_completed[i]
        i+=1
    return render(request, 'exam/viewstudents.html', {
        'students':dicts, 'examn':examn
    })
   

@login_required(login_url='faculty-login')
def view_results_prof(request):
    students = User.objects.filter(groups__name = "Student")
    dicts = {}
    prof = request.user
    professor = User.objects.get(username=prof.username)
    examn = Exam_Model.objects.filter(professor=professor)
    for exam in examn:
        if StuExam_DB.objects.filter(examname=exam.name,completed=1).exists():
            students_filter = StuExam_DB.objects.filter(examname=exam.name,completed=1)
            for student in students_filter:
                key = str(student.student.first_name + " " + student.student.last_name) + " " + str(student.examname) + " " +"results for " + str(student.qpaper.qPaperTitle)
                dicts[key] = student.score
    return render(request, 'exam/resultsstudent.html', {
        'students':dicts
    })

@login_required(login_url='login')
def view_exams_student(request):
    try:
        student = request.user.student
    

     # Get the grade level of the student
        grades = student.grade
    #subject = student.subject
        subjects = student.subject.all()
        exams = Exam_Model.objects.filter(subject__in=subjects, grade=grades, students=student).distinct() 
        list_of_completed = []
        list_un = []
        for exam in exams:
            if StuExam_DB.objects.filter(examname=exam.name ,student=request.user).exists():
                if StuExam_DB.objects.get(examname=exam.name,student=request.user).completed == 1:
                    list_of_completed.append(exam)
            else:
                list_un.append(exam)

        return render(request,'exam/mainexamstudent.html',{
            'exams':list_un,
            'completed':list_of_completed

        })
    except AttributeError:  # This error occurs when the user has no associated student
            template_name = 'exam/no_found_page.html'
    
    return render(request, template_name)

@login_required(login_url='login')
def view_students_attendance(request):
    student_s = request.user.student
    exams = Exam_Model.objects.filter(students=student_s)
    list_of_completed = []
    list_un = []
    for exam in exams:
        if StuExam_DB.objects.filter(examname=exam.name ,student=request.user).exists():
            if StuExam_DB.objects.get(examname=exam.name,student=request.user).completed == 1:
                list_of_completed.append(exam)
        else:
            list_un.append(exam)

    return render(request,'exam/attendance.html',{
        'exams':list_un,
        'completed':list_of_completed
    })

def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    min += hour*60
    return "%02d:%02d" % (min, sec) 

@login_required(login_url='login')
def appear_exam(request,id):
    student = request.user.first_name, request.user.last_name
    if request.method == 'GET':
        exam = Exam_Model.objects.get(pk=id)
        time_delta = exam.end_time - exam.start_time
        time = convert(time_delta.seconds)
        time = time.split(":")
        mins = time[0]
        secs = time[1]
        context = {
            "exam":exam,
            "question_list":exam.question_paper.questions.all(),
            "secs":secs,
            "mins":mins
        }
        return render(request,'exam/giveExam.html',context)
    if request.method == 'POST' :
        student = User.objects.get(first_name=request.user.first_name, last_name=request.user.last_name)
        paper = request.POST['paper']
        examMain = Exam_Model.objects.get(name = paper)
        stuExam = StuExam_DB.objects.get_or_create(examname=paper, student=student,qpaper = examMain.question_paper)[0]
        
        qPaper = examMain.question_paper
        stuExam.qpaper = qPaper
         
        qPaperQuestionsList = examMain.question_paper.questions.all()
        for ques in qPaperQuestionsList:
            student_question = Stu_Question(student=student,question=ques.question, optionA=ques.optionA, optionB=ques.optionB,optionC=ques.optionC, optionD=ques.optionD,
            answer=ques.answer)
            student_question.save()
            stuExam.questions.add(student_question)
            stuExam.save()

        stuExam.completed = 1
        stuExam.save()
        examQuestionsList = StuExam_DB.objects.filter(student=request.user,examname=paper,qpaper=examMain.question_paper,questions__student = request.user)[0]
        #examQuestionsList = stuExam.questions.all()
        examScore = 0
        list_i = examMain.question_paper.questions.all()
        queslist = examQuestionsList.questions.all()
        i = 0
        for j in range(list_i.count()):
            ques = queslist[j]
            max_m = list_i[i].max_marks
            ans = request.POST.get(ques.question, False)
            if not ans:
                ans = "E"
            ques.choice = ans
            ques.save()
            if ans.lower() == ques.answer.lower() or ans == ques.answer:
                examScore = examScore + max_m
            i+=1

        stuExam.score = examScore
        stuExam.save()
        stu = StuExam_DB.objects.filter(student=request.user,examname=examMain.name)  
        results = StuResults_DB.objects.get_or_create(student=request.user)[0]
        results.exams.add(stu[0])
        results.save()

     
        return redirect('view_exams_student')

@login_required(login_url='login')
def result(request,id):
    student = request.user
    exam = Exam_Model.objects.get(pk=id)
    score = StuExam_DB.objects.get(student=student,examname=exam.name,qpaper=exam.question_paper).score
    return render(request,'exam/result.html',{'exam':exam,"score":score})

###############################################################
#select from grade

def select_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade_id = form.cleaned_data['grade'].grade_name
           
            return redirect('grade_subjects', grade_id=grade_id)
    else:
        form = GradeForm()
    return render(request, 'exam/select_subject_grade.html', {'form': form})
############################
#filter out subjects
def grade_subjects(request, grade_id):
    
    grade = get_object_or_404(Grade, grade_name=grade_id)
    subjects = Subject.objects.filter(grade=grade)
    return render(request, 'exam/list_subject.html', {'grade': grade, 'subjects': subjects})

#view questions
def view_question(request, view_id, question_number):
    test = get_object_or_404(Exam_Model, test_name=view_id)
    question = questions.objects.filter(test=test, subject=question_number)
   # answers = Answer.objects.filter(number=question_number)
    return render(request, 'view_question.html', {'test': test, 'question': question})
###################################################
#assign students to exam type
def assign_test_to_students(request, grade_id, subject_id):
    
   
    grade = get_object_or_404(Grade, grade_name=grade_id)
    subject = get_object_or_404(Subject, subject_name=subject_id)
    
    students = Student.objects.filter(grade=grade, subject=subject)
    
    test = Exam_Model.objects.filter(grade=grade, subject=subject).first()
    
    if request.method == 'POST':
        
        form = TestAssignmentForm(request.POST, grade=grade, subject=subject)
        if form.is_valid():
            test.students.set(form.cleaned_data['students'])
           
            # Handle form submission here
            return redirect('success_page',grade_id=grade_id, subject_id=subject_id)  # Redirect to success page after assignment
    else:
        form = TestAssignmentForm(grade=grade, subject=subject)
        if not students:
            return render(request, 'exam/no_found_page.html')

    return render(request, 'exam/assign_test_to_students.html', {'form': form, 'grade': grade, 'subject': subject, 'test': test})