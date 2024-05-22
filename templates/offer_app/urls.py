from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('offer/<int:offer_id>/', views.offer_detail, name='offer_detail'),
    
    path('select_rate/<int:rate_id>/', views.select_rate, name='select_rate'),

    path('offer/<int:offer_id>/view', views.offer_view, name='offer_view'),

    path('api/get-message/<int:offer_id>/', views.api_get_message, name='api_get_message'),

    path('api/setoffer-status/<int:offer_id>/', views.api_client_offer_status, name='api_client_offer_status'),

    path('api/setoffer-delete/<int:offer_id>/', views.api_client_offer_delete, name='api_client_offer_delete'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)