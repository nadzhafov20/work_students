from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('offer/<int:offer_id>/', views.offer_detail, name='offer_detail'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)