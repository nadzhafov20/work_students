from django.urls import path
from . import views

urlpatterns = [
    path('student/settings', views.profile_settings, name='student_profile_settings'),
    path('student/my/', views.profile, name='student_profile'),
    path('student/career', views.career, name='student_career'),
    path('student/calendar', views.calendar, name='student_calendar'),
    path('student/offers', views.offers, name='student_offers'),
    path('student/close_account/', views.close_account, name='student_close_account'),
    path('student/portfolio', views.portfolio, name='student_portfolio'),
    path('student/my_jobs', views.my_jobs, name='student_my_jobs'),
]