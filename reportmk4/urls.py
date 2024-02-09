from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from reportmk4.views import reports_listmk4, update_drivermailmk4
from django.contrib import admin
from .views import update_report_mk4


urlpatterns = [
    path('indexmk4.html', views.indexmk4, name='indexmk4'),
    path('open_reportsmk4.html', views.reports_listmk4, name='reports_listmk4'),
    path('unit_historymk4.html', views.unit_historymk4, name='unit_historymk4'),
    # path('closed_reports.html', views.closed_reports_list, name='closed_reports_list'),
    path('report_detailmk4.html/<report_mk4_id>/', views.report_detailmk4, name='report_detailmk4'),
    path('my_reports/', views.my_reports, name='my_reports'), #
    path('add_reportmk4.html', views.add_reportmk4, name='add_reportmk4'),
    # path('my_messages/', views.my_messages, name='my_messages'),
    path('update_drivermk4.html', update_drivermailmk4, name='update_drivermk4'),
    path('update_report_mk4/<int:report_mk4_id>/', update_report_mk4, name='update_report_mk4'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)