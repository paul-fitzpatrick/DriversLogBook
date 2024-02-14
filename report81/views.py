from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import report_81
from django.contrib import messages
from .forms import ReportForm81, UpdateForm81
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import report_81
from django.views.generic import ListView
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


def index81(request):
    """ A view to return the index81 page """

    return render(request, 'index81.html')

# render report detail page
def report_detail81(request, report_81_id):
    """ A view to return the report details page """
    report81 = get_object_or_404(report_81, pk=report_81_id)

    # Get the previous and next items
    previous_item = report_81.objects.filter(id__lt=report_81_id).order_by('-id').first()
    next_item = report_81.objects.filter(id__gt=report_81_id).order_by('id').first()

    context = {
        'report81': report81,
        'prev_item': previous_item,
        'next_item': next_item,
    }

    return render(request, 'report_detail81.html', context)


# add report view
def add_report81(request):
    if request.method == "POST":
        form = ReportForm81(request.POST, request=request)
        if form.is_valid():
            form.instance.customer_email = request.user.email
            form.instance.name = request.user.username
            report81 = form.save(commit=False)
            report81.save()

            # Send an email using SendGrid
            try:
                # Get form data
                car = form.cleaned_data['car']
                ref_number = form.cleaned_data['ref_number']
                defect_details = form.cleaned_data['defect_details']
                driver_email = form.cleaned_data['driver_email']
                driver_name = form.cleaned_data['driver_name']
                date_of_fault = form.cleaned_data['date_of_fault']
                location_at_time_of_fault = form.cleaned_data['location_at_time_of_fault']

                # Create a SendGrid message
                sendgrid_message = Mail(
                    from_email=request.user.email,
                    to_emails=driver_email,
                    subject=f'Report for {car}, ref#{ref_number}',
                    html_content=f'Hi {driver_name}, <br> Your report on {date_of_fault}, that unit {car} had the following issue:{defect_details},at {location_at_time_of_fault}, has been emailed to drogheda dsm. ',
                )

                # Initialize the SendGrid client with your API key
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

                # Send the email
                response = sg.send(sendgrid_message)

                # Check if the email was sent successfully
                if response.status_code == 202:
                    messages.success(request, 'Thank you for submitting the report. An email has been sent to the driver.')
                else:
                    messages.error(request, 'Failed to send the email. Please try again later.')

            except Exception as e:
                # Handle exceptions, e.g., log the error
                error_message = str(e)
                if 'Unauthorized' in error_message:
                    messages.error(request, 'Authentication error. Please check your SendGrid API key.')
                else:
                    messages.error(request, f'An error occurred while sending the email: {error_message}')

            return redirect('open_reports81.html')  # Redirect to the desired page after adding the report
    else:
        form = ReportForm81(request=request)
    
    context = {
        'form': form,
        'report81_added': True,
    }
    
    return render(request, 'add_report81.html', context)


# Search box and open reports view
def reports_list81(request):
    """ A View to return all read/work order reports and search queries """

    reports81 = report_81.objects.all() 
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey    
            reports81 = reports81.order_by(sortkey)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter anything to search"))
                return redirect('/')

            queries = Q(car__icontains=query) | Q(defect_keyword__icontains=query)   
            reports81 = reports81.filter(queries)
    current_sorting = f'{sort}_{direction}'

    context = {
        'reports81': reports81,
        'search_term': query,
        
        'current_sorting': current_sorting,
    }
    return render(request, 'open_reports81.html', context)


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        return super().default(obj)


# my report page
# def my_reports(request):
#     # Retrieve the user's reports
#     reports = report_81.objects.filter(driver_email=request.user.email)

#     # Serialize the reports to JSON using the custom encoder
#     reports_json = json.dumps(list(reports.values()), cls=CustomJSONEncoder)

#     context = {
#         'reports_json': reports_json,
#         'reports': reports
#     }

#     return render(request, 'my_reports.html', context)


# unit history search box
def unit_history81(request):
    """ A View to return all read/work order reports and search queries """

    reports81 = report_81.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey    
            reports81 = reports81.order_by(sortkey)
        
        if 'u' in request.GET:
            query = request.GET['u']
            if not query:
                messages.error(request, "You didn't enter anything to search")
                return redirect('index81')

            last_two_numbers = query[-2:]  # Extract the last two numbers from the query
            queries = Q(car__endswith=last_two_numbers)   
            reports81 = reports81.filter(queries)

            if not reports81.exists():  # Check if there are no results
                messages.info(request, f"There are no results for '{query}'")
                return redirect('/', {'search_term': query})

    current_sorting = f'{sort}_{direction}'

    context = {
        'reports81': reports81,
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'unit_history81.html', context)


# def my_messages81(request):
#     messages = report_81.objects.filter(driver_name=request.user.username).order_by('-date_of_fault')
#     return render(request, 'my_messages.html', {'messages': messages})


def update_driver_view81(request):
    return render(request, 'update_driver81.html')


def update_drivermail81(request):
    form = UpdateForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return redirect('open_reports81.html')  # Redirect to the desired URL after form submission

    context = {
        'form': form,
    }
    
    return render(request, 'update_driver81.html', context)
    

# hidden form for emailing drivers of update
def update_report_81(request, report_81_id):
    report_81 = get_object_or_404(report_81, pk=report_81_id)

    if request.method == 'POST':
        # Handle the form submission
        form = UpdateForm(request.POST, instance=report_81)
        if form.is_valid():
            form.save()
            # Send email code here
            return redirect('admin:report_report_81_changelist')  # Redirect to the changelist view
    else:
        # Display the form
        form = UpdateForm(instance=report_81)

    return render(request, 'update_driver81.html', {'form': form})