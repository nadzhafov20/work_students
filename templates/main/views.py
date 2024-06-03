from django.shortcuts import render, redirect
from .forms import LoginForm, StudentRegistrationForm, ClientRegistrationForm
from django.contrib.auth import login
from .utils.send_email import send_mail_using_sendgrid
from django.conf import settings
from django.template.loader import render_to_string
import secrets
from main.models import MyUser
from django.http import HttpResponse
from .utils.statistics import technology_statistics
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                return redirect('student_offers')
            elif request.user.role == 'client':
                return redirect('client_students')
    context = technology_statistics()
    return render(request, 'home/index.html', context)

def choose_role(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                return redirect('student_profile')
            elif request.user.role == 'client':
                return redirect('student_profile')
    return render(request, 'home/choose_role.html')

def success_view(request):
    return render(request, 'home/success.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('student_profile' if user.role == 'student' else 'client_profile')
    else:
        form = LoginForm()
    if request.user.is_authenticated:
        if hasattr(request.user, 'role'):
            if request.user.role == 'student':
                return redirect('student_profile')
            elif request.user.role == 'client':
                return redirect('student_profile')
    return render(request, 'home/login.html', {'form': form})

@login_required
def close_account(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('student_profile')

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            verif_tokent = secrets.token_urlsafe(16)
            user = form.save(commit=False)
            #user.username = form.cleaned_data['email']
            user.role = 'student'
            user.set_password(form.cleaned_data['password'])
            user.verification_token = verif_tokent
            user.save()            
            
            activation_link = f'http://127.0.0.1:8000/verify-email/{verif_tokent}'
            html_constent = render_to_string('email/email_confirmation_student.html', {'name': form.cleaned_data['first_name'], 'activation_link': activation_link})
            send_mail_using_sendgrid(
                api_key=settings.EMAIL_API_KEY,
                from_email=settings.EMAIL_FROM,
                to_emails=form.cleaned_data['email'], 
                subject='Email confirmation', 
                html_content=html_constent)

            #StudentModel.objects.create(user=user)
            login(request, user)
            return redirect('success_url')
    else:
        form = StudentRegistrationForm()
    return render(request, 'home/register_student.html', {'form': form})

def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            verif_tokent = secrets.token_urlsafe(16)
            user = form.save(commit=False)
            #user.username = form.cleaned_data['email']
            user.role = 'client'
            user.set_password(form.cleaned_data['password'])
            user.verification_token = verif_tokent
            user.save()            
            #ClientModel.objects.create(user=user)
            login(request, user)
            return redirect('success_url')
    else:
        form = ClientRegistrationForm()
    return render(request, 'home/register_client.html', {'form': form})

def verify_email(request, token):
    try:
        user = MyUser.objects.get(verification_token=token)
        user.email_verified = True
        user.save()
        return redirect('login')
    except MyUser.DoesNotExist:
        return HttpResponse('Ссылка для подтверждения почты недействительна!')
    
def about_us(request):
    return render(request, 'home/about_us.html')

def community(request):
    return render(request, 'home/community.html')

def cookie_policy(request):
    return render(request, 'home/cookie_policy.html')

def help_support(request):
    return render(request, 'home/help_support.html')

def cookie_settings(request):
    return render(request, 'home/cookie_settings.html')

def terms_of_service(request):
    return render(request, 'home/terms_of_service.html')

def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')