from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report201.views import reports_list201, update_drivermail201
from django.contrib import admin
from .views import update_report_201


urlpatterns = [
    path('index201.html', views.index201, name='index201'),
    path('open_reports201.html', views.reports_list201, name='reports_list201'),
    path('unit_history201.html', views.unit_history201, name='unit_history201'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail201.html/<report_201_id>/', views.report_detail201, name='report_detail201'),
    path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report201.html', views.add_report201, name='add_report201'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver201.html', update_drivermail201, name='update_driver201'),
    path('update_report_201/<int:report_201_id>/', update_report_201, name='update_report_201'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)