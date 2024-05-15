from django.shortcuts import render, redirect
from main.models import MyUser
from offer_app.models import OffersModel
from student.models import SetQualificationStudentModel, SetStudentSkilsModel, StudentCalendarModel
from django.http import JsonResponse



def profile(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'client':
                return render(request, 'client/profile.html', {'user': request.user})
            elif request.user.role == 'student':
                return redirect('student_profile')
    return redirect('login')

def students(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'client':
                students = MyUser.objects.filter(role='student')
                qualifications = SetQualificationStudentModel.objects.all()
                skills = SetStudentSkilsModel.objects.all()

                qualification_id = request.GET.get('qualification')
                skill_id = request.GET.get('skill')
                start_date = request.GET.get('start_date')
                end_date = request.GET.get('end_date')

                print(qualification_id)
                print(skill_id)
                print(start_date)
                print(end_date)

                if qualification_id:
                    students = students.filter(qualification_id=qualification_id)
                if skill_id:
                    students = students.filter(skils__id=skill_id)
                if start_date and end_date:
                    busy_students = StudentCalendarModel.objects.filter(date__range=[start_date, end_date]).values_list('user_id', flat=True)
                    students = students.exclude(id__in=busy_students)

                context = {
                    'user': request.user,
                    'students': students,
                    'qualifications':qualifications,
                    'skills':skills,
                }

                return render(request, 'client/students.html', context)
            
def client_my_offers(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'client':
                user = request.user
                offers = OffersModel.objects.filter(user_client=user)
                return render(request, 'client/my_offers.html', {'offers':offers,'user':user})
            