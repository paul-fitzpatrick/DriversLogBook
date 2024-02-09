from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report071.views import reports_list071, update_drivermail071
from django.contrib import admin
from .views import update_report_071


urlpatterns = [
    path('index071.html', views.index071, name='index071'),
    path('open_reports071.html', views.reports_list071, name='reports_list071'),
    path('unit_history071.html', views.unit_history071, name='unit_history071'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail071.html/<report_071_id>/', views.report_detail071, name='report_detail071'),
    path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report071.html', views.add_report071, name='add_report071'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver071.html', update_drivermail071, name='update_driver071'),
    path('update_report_071/<int:report_071_id>/', update_report_071, name='update_report_071'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)