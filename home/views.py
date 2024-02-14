from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from report26.models import report_26
from report28.models import report_28
from report29.models import report_29
from report22.models import report_22
from report81.models import report_81
from report85.models import report_85
from report201.models import report_201
from reportmk4.models import report_mk4
from report071.models import report_071
import logging
import json


def index(request):
    """ A view to return the index page """

    return render(request, 'index.html')


def about(request):
    """ A view to return the index page """

    return render(request, 'about.html')

###test

# my report page
@login_required
def my_all_reports(request):
    # Retrieve reports from all apps for the logged-in user
    user_email = request.user.email
    
    # Retrieve reports from all relevant models
    reports_26 = report_26.objects.filter(driver_email=user_email)
    reports_28 = report_28.objects.filter(driver_email=user_email)
    reports_29 = report_29.objects.filter(driver_email=user_email)
    reports_22 = report_22.objects.filter(driver_email=user_email)
    reports_071 = report_071.objects.filter(driver_email=user_email)
    reports_81 = report_81.objects.filter(driver_email=user_email)
    reports_85 = report_85.objects.filter(driver_email=user_email)
    reports_201 = report_201.objects.filter(driver_email=user_email)
    reports_mk4 = report_mk4.objects.filter(driver_email=user_email)
    
    # Combine all reports into a single queryset
    all_reports = list(reports_26) + list(reports_28) + list(reports_29) + \
                  list(reports_22) + list(reports_071) + list(reports_81) + \
                  list(reports_85) + list(reports_201) + list(reports_mk4)

    context = {
        'all_reports': all_reports
    }

    return render(request, 'my_all_reports.html', context)

#