from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from offer_app.models import OffersModel
from student.models import EducationStudentModel, PortfolioStudentModel, SetQualificationStudentModel, SetStudentSkilsModel
from datetime import datetime
from django.http import JsonResponse
import datetime
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import MyUser
from offer_app.models import OffersModel
from .forms import PersonalinfoSettingForm, EducationStudentForm, LanguageStudentForm
from django.forms import inlineformset_factory
from .models import LanguageStudentModel
from utils.decorators import user_is_authenticated, email_verified_required, role_required
from utils.time_utils import current_time_user_tz
from django.views import View
from django.utils.decorators import method_decorator
from .utils.calendar_utils import (update_calendar_entries,get_month_calendar_data,get_user_events,format_dates,annotate_calendar_with_status)
from .utils.total_percent import calculate_total_percent


@user_is_authenticated
@email_verified_required
@role_required('student')
def profile_settings(request):
    user = request.user
    EducationFormSet = inlineformset_factory(MyUser, EducationStudentModel, form=EducationStudentForm, extra=1, can_delete=True)
    LanguageStudentFormSet = inlineformset_factory(MyUser, LanguageStudentModel, form=LanguageStudentForm, extra=1, can_delete=True)
    if request.method == 'POST':
        data = request.POST
        personal_info_form = PersonalinfoSettingForm(request.POST, request.FILES, instance=user, prefix='personal')
        education_formset = EducationFormSet(request.POST, instance=user, prefix='education')
        language_formset = LanguageStudentFormSet(request.POST, instance=user, prefix='language')

        if personal_info_form.is_valid() and education_formset.is_valid() and language_formset.is_valid():
            personal_info_form.save()
            education_formset.save()
            language_formset.save()

            return redirect('student_profile_settings')

        print(data)
    else:
        qualifications = SetQualificationStudentModel.objects.all()
        personal_info_form = PersonalinfoSettingForm(instance=user, prefix='personal')
        education_formset = EducationFormSet(instance=user, prefix='education')
        language_formset = LanguageStudentFormSet(instance=user, prefix='language')
        context = {
            'personal_info_form': personal_info_form,
            'education_formset': education_formset,
            'language_formset': language_formset,
            'user': user
        }
        return render(request, 'student/profile_settings.html', context)

@user_is_authenticated
@email_verified_required
@role_required('student')
def my_jobs(request):
    user = request.user
    offers = OffersModel.objects.filter(user_student=user)
    return render(request, 'student/my_jobs.html', {'offers':offers, 'user':user})


@user_is_authenticated
@email_verified_required
@role_required('student')
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
    else:
        return render(request, 'student/portfolio.html')

@user_is_authenticated
@email_verified_required
@role_required('student')
def profile(request):
    user=request.user
    portfolio = PortfolioStudentModel.objects.filter(user=user)
    educations = EducationStudentModel.objects.filter(user=user)
    languages = LanguageStudentModel.objects.filter(user=user)
    context = {
        'user':user,
        'portfolio':portfolio,
        'educations':educations,
        'languages':languages,
        'current_time_user_tz': current_time_user_tz(str(user.time_zone))
    }
    return render(request, 'student/profile.html', context)
    
@method_decorator([user_is_authenticated, email_verified_required, role_required('student')], name='dispatch')
class CareerView(View):
    def get(self, request):
        qualifications = SetQualificationStudentModel.objects.all()
        skills = SetStudentSkilsModel.objects.all()

        context = {
            'qualifications': qualifications,
            'skills': skills,
        }

        return render(request, 'student/career_profile.html', context)

    def post(self, request):
        qualification_id = request.POST.get('qualification')
        project_direction_id = request.POST.get('project_direction')
        tool_id = request.POST.get('skill')

        qualification = SetQualificationStudentModel.objects.get(id=qualification_id)
        user = request.user
        user.qualification = qualification
        user.save()

        return redirect('student_profile')


@method_decorator([user_is_authenticated, email_verified_required, role_required('student')], name='dispatch')
class CalendarView(View):
    def post(self, request):
        data = json.loads(request.body)
        update_calendar_entries(request.user, data)
        return JsonResponse({'success': True})

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        today = datetime.date.today()
        year = int(request.GET.get('year', today.year))
        months_data = get_month_calendar_data(year)
        events, busy_dates, slightly_busy_dates = get_user_events(request.user)
        formatted_busy_dates = format_dates(busy_dates, year)
        formatted_slightly_busy_dates = format_dates(slightly_busy_dates, year)
        months_data = annotate_calendar_with_status(months_data, busy_dates, slightly_busy_dates, year)

        context = {
            'months_data': months_data,
            'current_year': year,
            'year': year,
            'today': today,
            'events': events,
            'busy_dates': formatted_busy_dates,
            'slightly_busy_dates': formatted_slightly_busy_dates,
        }
        return render(request, 'student/calendar.html', context)

@user_is_authenticated
@email_verified_required
@role_required('student')
def offers(request):
    offers = OffersModel.objects.all()
    student = request.user
    total_percent = calculate_total_percent(student)

    return render(request, 'student/offers.html', {'offers': offers, 'user':request.user, 'rating_percent': total_percent})

def public_view(request, username):
    student = MyUser.objects.get(username=username)
    portfolio = PortfolioStudentModel.objects.filter(user=student.id)
    educations = EducationStudentModel.objects.filter(user=student)
    languages = LanguageStudentModel.objects.filter(user=student)
    print(portfolio)
    context = {
        'student':student,
        'portfolio':portfolio,
        'current_time_user_tz':current_time_user_tz(str(student.time_zone)),
        'educations':educations,
        'languages':languages,
        }
    return render(request, 'student/public_view.html', context)