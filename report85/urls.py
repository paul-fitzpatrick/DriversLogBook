from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report85.views import reports_list85, update_drivermail85
from django.contrib import admin
from .views import update_report_85


urlpatterns = [
    path('index85.html', views.index85, name='index85'),
    path('open_reports85.html', views.reports_list85, name='reports_list85'),
    path('unit_history85.html', views.unit_history85, name='unit_history85'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail85.html/<report_85_id>/', views.report_detail85, name='report_detail85'),
    #path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report85.html', views.add_report85, name='add_report85'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver85.html', update_drivermail85, name='update_driver85'),
    path('update_report_85/<int:report_85_id>/', update_report_85, name='update_report_85'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)