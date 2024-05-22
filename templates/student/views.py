from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from offer_app.models import OffersModel
from calendar import monthcalendar
from student.models import StudentCalendarModel, EducationStudentModel, PortfolioStudentModel, SetQualificationStudentModel, SetStudentSkilsModel
from django import template
from datetime import datetime
from django.http import JsonResponse
import datetime
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import MyUser
from pytz import all_timezones
from timezone_field import TimeZoneFormField
from offer_app.models import OffersModel
from .forms import PersonalinfoSettingForm, EducationStudentForm
from django.forms import inlineformset_factory
import pytz


register = template.Library()

from django.utils import timezone

def current_time_user_tz(user_time_zone):
    current_time_utc = timezone.now()
    user_tz = pytz.timezone(user_time_zone)
    current_time_user_tz = current_time_utc.astimezone(user_tz)
    formatted_event_time = current_time_user_tz.strftime('%I:%M %p').lower()
    return formatted_event_time


def profile_settings(request):
    user = request.user
    EducationFormSet = inlineformset_factory(MyUser, EducationStudentModel, form=EducationStudentForm, extra=1, can_delete=True)

    if request.method == 'POST':
        data = request.POST
        personal_info_form = PersonalinfoSettingForm(request.POST, request.FILES, instance=user, prefix='personal')
        education_formset = EducationFormSet(request.POST, instance=user, prefix='education')

        if personal_info_form.is_valid() and education_formset.is_valid():
            personal_info_form.save()
            education_formset.save()

            return redirect('student_profile_settings')

        print(data)

    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                qualifications = SetQualificationStudentModel.objects.all()
                personal_info_form = PersonalinfoSettingForm(instance=user, prefix='personal')
                education_formset = EducationFormSet(instance=user, prefix='education')
                context = {
                    'personal_info_form': personal_info_form,
                    'education_formset': education_formset,
                    'user': user
                }
                return render(request, 'student/profile_settings.html', context)
            elif request.user.role == 'client':
                return redirect('client_profile')
    return redirect('login')

def my_jobs(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                user = request.user
                offers = OffersModel.objects.filter(user_student=user)
                return render(request, 'student/my_jobs.html', {'offers':offers, 'user':user})

def portfolio(request):
    if request.method == 'POST':
        image = request.FILES.get("image")
        title = 'Title'
        description = 'Description'
        portfolio = PortfolioStudentModel(
            user=request.user,
            title=title,
            description=description,
            photo=image
        )
        portfolio.save()

        return HttpResponseRedirect(reverse('student_profile'))


    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                return render(request, 'student/portfolio.html')

def profile(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                user=request.user
                portfolio = PortfolioStudentModel.objects.filter(user=user)
                educations = EducationStudentModel.objects.filter(user=user)
                context = {
                    'user':user,
                    'portfolio':portfolio,
                    'educations':educations,
                    'current_time_user_tz': current_time_user_tz(str(user.time_zone))
                }

                return render(request, 'student/profile.html', context)
            elif request.user.role == 'client':
                return redirect('student_profile')
    return redirect('login')

@login_required
def close_account(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('student_profile')
    
def career(request):
    if request.method == 'POST':
        qualification_id = request.POST.get('qualification')
        project_direction_id = request.POST.get('project_direction')
        tool_id = request.POST.get('skill')
        print('Qualification ID:', qualification_id)
        print('Project Direction ID:', project_direction_id)
        print('Tool ID:', tool_id)

        qualification = SetQualificationStudentModel.objects.get(id=qualification_id)
        user = request.user
        user.qualification = qualification
        user.save()


        return redirect('student_profile')
    else:
        if request.user.is_authenticated:
            qualifications = SetQualificationStudentModel.objects.all()
            skills = SetStudentSkilsModel.objects.all()

            context = {
                'qualifications': qualifications,
                'skills': skills,
            }

            return render(request, 'student/career_profile.html', context)
        else:
            return redirect('student_career')

def calendar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        today = datetime.date.today()
        for entry in data:
            user = request.user
            first_entry = data[0] 
            year = first_entry.get('year', today.year)
            date = datetime.date(year=year, month=int(entry['month']), day=int(entry['day']))
            status = entry['status']
            if status == 'B':
                StudentCalendarModel.objects.update_or_create(user=user, date=date, status='red')
            if status == 'S':
                StudentCalendarModel.objects.update_or_create(user=user, date=date, status='yellow')
            if status == 'N':
                calendar = StudentCalendarModel.objects.filter(user=user, date=date)
                calendar.delete()
            else:
                StudentCalendarModel.objects.update_or_create(user=user, date=date, status=None)
        return JsonResponse({'success': True})
    else:
        month_names = ['January', 'February', 'March', 'April', 'May',
                    'June', 'July', 'August', 'September', 'October',
                    'November', 'December']
        
        if request.user.is_authenticated:
            today = datetime.date.today()
            year = request.GET.get('year', today.year)

            current_year = int(year)

            months_data = []
            for month in range(1, 13):
                month_calendar = monthcalendar(current_year, month)
                month_data = {
                    'month_name': month_names[month - 1],
                    'month_number': month,
                    'month_calendar': month_calendar,
                }
                months_data.append(month_data)

            events = StudentCalendarModel.objects.filter(user=request.user)

            busy_dates = [event.date for event in events if event.status == 'red']
            slightly_busy_dates = [event.date for event in events if event.status == 'yellow']

            formatted_busy_dates = [{'year': year, 'month': date.month, 'day': date.day} for date in busy_dates]
            formatted_slightly_busy_dates = [{'year': year, 'month': date.month, 'day': date.day} for date in slightly_busy_dates]


            for month_data in months_data:
                month = month_data['month_number']
                for week in month_data['month_calendar']:
                    for day in week:
                        if day != 0:
                            for busy_date in busy_dates:
                                if busy_date.year == current_year and busy_date.month == month and busy_date.day == day:
                                    status = 'B'
                                    break
                            else:
                                for sl_busy_date in slightly_busy_dates:
                                    if sl_busy_date.year == current_year and sl_busy_date.month == month and sl_busy_date.day == day:
                                        status = 'S'
                                        break
                                else:
                                    status = 'F'
                            day_index = month_data['month_calendar'].index(week)
                            month_data['month_calendar'][day_index][week.index(day)] = {'day': day, 'status': status}

            context = {
                'months_data': months_data,
                'current_year': current_year,
                'year': year,
                'today': today, 
                'events': events,
                'busy_dates': formatted_busy_dates,
                'slightly_busy_dates': formatted_slightly_busy_dates,
            }
            return render(request, 'student/calendar.html', context)
        
        return redirect('login')

def offers(request):
    offers = OffersModel.objects.all()

    student = request.user

    total_percent = 0
    total_percent += 20 if student.qualification else 0
    total_percent += 20 if student.price_hour else 0
    total_percent += 10 if student.image else 0
    total_percent += 20 if student.about else 0
    total_percent += 30 if student.address else 0

    return render(request, 'student/offers.html', {'offers': offers, 'user':request.user, 'rating_percent': total_percent})

def public_view(request, username):
    student = MyUser.objects.get(username=username)
    portfolio = PortfolioStudentModel.objects.filter(user=student.id)
    print(portfolio)
    context = {
        'student':student,
        'portfolio':portfolio,
        'current_time_user_tz':current_time_user_tz(str(student.time_zone))
        }
    return render(request, 'student/public_view.html', context)