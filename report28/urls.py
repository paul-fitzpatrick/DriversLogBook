from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report28.views import reports_list28, update_drivermail28
from django.contrib import admin
from .views import update_report_28


urlpatterns = [
    path('index28.html', views.index28, name='index28'),
    path('open_reports28.html', views.reports_list28, name='reports_list28'),
    path('unit_history28.html', views.unit_history28, name='unit_history28'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail28.html/<report_28_id>/', views.report_detail28, name='report_detail28'),
    #path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report28.html', views.add_report28, name='add_report28'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver28.html', update_drivermail28, name='update_driver28'),
    path('update_report_28/<int:report_28_id>/', update_report_28, name='update_report_28'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)