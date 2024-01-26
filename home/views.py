from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from report.models import report29
from django.core.mail import send_mail, BadHeaderError
import logging


def index(request):
    """ A view to return the index page """

    return render(request, 'index.html')
