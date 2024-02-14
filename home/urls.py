from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('my-all-reports/', views.my_all_reports, name='my_all_reports'),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)