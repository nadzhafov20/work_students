from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('choose_role/', views.choose_role, name='choose_role'),
    path('login/', views.login_view, name='login'),
    
    path('register/student', views.register_student, name='register_student'),
    path('register/client', views.register_client, name='register_client'),

    path('success/', views.success_view, name='success_url'),

    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),

    path('about_us', views.about_us, name='about_us'),
    path('community', views.community, name='community'),
    path('cookie_policy', views.cookie_policy, name='cookie_policy'),
    path('help_support', views.help_support, name='help_support'),
    path('cookie_settings', views.cookie_settings, name='cookie_settings'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)