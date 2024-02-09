from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report26.views import reports_list26, update_drivermail26
from django.contrib import admin
from .views import update_report_26


urlpatterns = [
    path('index26.html', views.index26, name='index26'),
    path('open_reports26.html', views.reports_list26, name='reports_list26'),
    path('unit_history26.html', views.unit_history26, name='unit_history26'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detail26.html/<report_26_id>/', views.report_detail26, name='report_detail26'),
    path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_report26.html', views.add_report26, name='add_report26'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_driver26.html', update_drivermail26, name='update_driver26'),
    path('update_report_26/<int:report_26_id>/', update_report_26, name='update_report_26'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)