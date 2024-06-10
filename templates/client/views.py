from django.shortcuts import render, redirect
from main.models import MyUser, NotificationsModel
from offer_app.models import OffersModel
from student.models import SetQualificationStudentModel, SetStudentSkilsModel, StudentCalendarModel
from datetime import datetime

from client.models import OfferJobModel
from .forms import OffersModelForm, PersonalinfoSettingForm, OfferJobForm
from utils.decorators import user_is_authenticated, email_verified_required, role_required


@user_is_authenticated
@email_verified_required
@role_required('client')
def profile(request):
    user = request.user
    if request.method == 'POST':
        personal_info_form = PersonalinfoSettingForm(request.POST, request.FILES, instance=user, prefix='personal')
        data = request.POST
        if personal_info_form.is_valid():
            personal_info_form.save()
            return redirect('client_profile')
        else:
            return redirect('client_profile')
    else:
        personal_info_form = PersonalinfoSettingForm(instance=user, prefix='personal')
        context = {
            'user': request.user,
            'personal_info_form': personal_info_form,
            }
        return render(request, 'client/profile.html', context)


@user_is_authenticated
@email_verified_required
@role_required('client')
def students(request):
    students = MyUser.objects.filter(role='student')
    qualifications = SetQualificationStudentModel.objects.all()
    skills = SetStudentSkilsModel.objects.all()

    qualification_id = request.GET.get('qualification')
    skill_id = request.GET.get('skill')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    if qualification_id:
        students = students.filter(qualification_id=qualification_id)
    if skill_id:
        students = students.filter(skils__id=skill_id)
    if start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None
        busy_students = StudentCalendarModel.objects.filter(date__range=[start_date, end_date]).values_list('user_id', flat=True)
        students = students.exclude(id__in=busy_students)
        
    context = {
        'user': request.user,
        'students': students,
        'qualifications':qualifications,
        'skills':skills,
    }

    return render(request, 'client/students.html', context)

@user_is_authenticated
@email_verified_required
@role_required('client')   
def client_my_offers(request):
    user = request.user
    offers = OffersModel.objects.filter(user_client=user)
    return render(request, 'client/my_offers.html', {'offers':offers,'user':user})


@user_is_authenticated
@email_verified_required
@role_required('client') 
def add_offer(request):
    user = request.user
    if request.method == 'POST':
        data = request.POST
        form = OffersModelForm(request.POST)
        print(data)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('client_my_offers')
    else:
        user = request.user
        form = OffersModelForm()
        return render(request, 'client/add_offer.html', {'form':form})

from django.contrib.contenttypes.models import ContentType

@user_is_authenticated
@email_verified_required
@role_required('client')
def offer_job(request, username):
    user = request.user
    student = MyUser.objects.get(username=username)

    if request.method == 'POST':
        form = OfferJobForm(request.POST)
        if form.is_valid():
            offer_job_instance = form.save(commit=True, user=user, student=student)
            message = f'Client {user.first_name} {user.last_name} offered you a job'
            content_type = ContentType.objects.get_for_model(OfferJobModel)
            nt = NotificationsModel.objects.create(
                user_id=student,
                message=message,
                object_id=offer_job_instance.id,
                content_type=content_type
            )
            return redirect('client_profile')
    else:
        form = OfferJobForm()
        context = {
            'form': form,
            'student': student,
            'user': user
        }
        return render(request, 'client/offer_job.html', context)