from django.urls import path
from . import views


urlpatterns = [
    path('client/my', views.profile, name='client_profile'),
    path('client/students/', views.students, name='client_students'),
    path('client/offers', views.client_my_offers, name='client_my_offers'),
    path('client/add_offer', views.add_offer, name='client_add_offer')
]