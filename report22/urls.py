from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report22.views import reports_list22, update_drivermail22
from django.contrib import admin
from .views import update_report_22


urlpatterns = [
    path('index22.html', views.index22, name='index22'),
    path('open_reports22.html', views.reports_list22, name='reports_list22'),
    path('unit_history22.html', views.unit_history22, name='unit_history22'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail22.html/<report_22_id>/', views.report_detail22, name='report_detail22'),
    path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report22.html', views.add_report22, name='add_report22'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver22.html', update_drivermail22, name='update_driver22'),
    path('update_report_22/<int:report_22_id>/', update_report_22, name='update_report_22'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)