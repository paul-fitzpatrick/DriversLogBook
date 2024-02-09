from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report81.views import reports_list81, update_drivermail81
from django.contrib import admin
from .views import update_report_81


urlpatterns = [
    path('index81.html', views.index81, name='index81'),
    path('open_reports81.html', views.reports_list81, name='reports_list81'),
    path('unit_history81.html', views.unit_history81, name='unit_history81'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail81.html/<report_81_id>/', views.report_detail81, name='report_detail81'),
    path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report81.html', views.add_report81, name='add_report81'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver81.html', update_drivermail81, name='update_driver81'),
    path('update_report_81/<int:report_81_id>/', update_report_81, name='update_report_81'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)