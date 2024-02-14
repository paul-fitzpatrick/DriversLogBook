from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report29.views import reports_list29, update_drivermail29
from django.contrib import admin
from .views import update_report_29


urlpatterns = [
    path('index29.html', views.index29, name='index29'),
    path('open_reports29.html', views.reports_list29, name='reports_list29'),
    path('unit_history29.html', views.unit_history29, name='unit_history29'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail29.html/<report_29_id>/', views.report_detail29, name='report_detail29'),
    #path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report29.html', views.add_report29, name='add_report29'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver29.html', update_drivermail29, name='update_driver29'),
    path('update_report_29/<int:report_29_id>/', update_report_29, name='update_report_29'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)