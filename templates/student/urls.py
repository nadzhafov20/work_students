from django.urls import path
from . import views
from .views import CalendarView, CareerView

urlpatterns = [
    path('student/settings', views.profile_settings, name='student_profile_settings'),
    path('student/my/', views.profile, name='student_profile'),
    path('student/career', CareerView.as_view(), name='student_career'),
    path('student/calendar', CalendarView.as_view(), name='student_calendar'),
    path('student/offers', views.offers, name='student_offers'),
    path('student/portfolio', views.portfolio, name='student_portfolio'),
    path('student/my_jobs', views.my_jobs, name='student_my_jobs'),
    path('view/profile/<str:username>', views.public_view, name='student_public_view'),
    path('student/notifications', views.notifications_views, name='student_notifications'),
    path('student/notification/<int:id>', views.notification_view, name='student_notification_view'),

    path('api/user/delete-photo', views.delete_photo, name='delete_photo'),
    path('api/user/delete-video_introduction', views.delete_video_introduction, name='delete_video_introduction'),
]