from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from .models import report_28
from django.shortcuts import render
from .forms import UpdateForm28
import json
import requests
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.contrib import messages
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


@admin.register(report_28)
class report_28Admin(admin.ModelAdmin):
    search_fields = ('car', 'date_of_fault', 'defect_keyword', 'ref_number')
    list_display = ('car', 'date_of_fault', 'ref_number', 'driver_name', 'report_read', 'work_order_created', 'work_order_closed', 'driver_emailed')
    actions = ['download_information28', 'send_email_action', 'pdf_download']  # Registering the custom actions

    def approve_report(self, request, queryset):
        queryset.update(report_approved=True)

    def download_information28(self, request, queryset):
        # Define the fields to include in the downloaded file
        fields = ['Grade', 'driver_name', 'driver_email', 'car', 'location_at_time_of_fault',
                  'time_of_fault', 'date_of_fault', 'defect_keyword', 'defect_details',
                  'ref_number', 'report_read', 'work_order_created', 'driver_emailed',
                  'work_order_closed', 'work_order_number', 'Depot_feedback', 'status_changed']

        # Generate the CSV content
        csv_content = ','.join(fields) + '\n'
        for obj in queryset:
            row = [str(getattr(obj, field)) for field in fields]
            csv_content += ','.join(row) + '\n'

        # Create the response with the CSV content
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="logbook_report_information.csv"'
        response.write(csv_content)
        return response

    download_information28.short_description = 'Download Logbook Report CSV'  # Action description for the admin interface

    def approve_report(self, request, queryset):
        queryset.update(report_approved=True, status_changed=True)

    approve_report.short_description = 'Approve Selected Reports'  # Action description for the admin interface

    
    def send_email_action(self, request, queryset):
        selected_drivers = []
        selected_cars = []
        selected_depots = []
        selected_refs = []
        selected_dates = []
        selected_defects = []

        for obj in queryset:
            selected_drivers.append(obj.driver_email)
            selected_cars.append(obj.car)
            selected_depots.append(obj.Depot_feedback)
            selected_refs.append(obj.ref_number)
            selected_dates.append(obj.date_of_fault)
            selected_defects.append(obj.defect_details)

        # Compose and send email using SendGrid
        try:
            # Compose your email content here
             # Compose your email content here
            subject = f'Report for {car}, ref#{ref_number}'
            message = f'Hi {driver_name}, <br> Your report on {date_of_fault}, that unit {car} had the following issue:{defect_details},at {location_at_time_of_fault}, has had its issue repaired. <br> The following information has been provided by the depot: <br>{work_order_number} <br> {Depot_feedback} '
            from_email = 'paul.fitzpatrick@irishrail.ie'  # Replace with your SendGrid verified email
            recipient_list = selected_drivers

            # Create a SendGrid message
            sendgrid_message = Mail(
                from_email=from_email,
                to_emails=recipient_list,
                subject=subject,
                html_content=message,
            )

            # Initialize the SendGrid client with your API key
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

            # Send the email
            response = sg.send(sendgrid_message)

            # Check if the email was sent successfully
            if response.status_code == 202:
                messages.success(request, 'Update emails sent successfully.')
            else:
                messages.error(request, 'Failed to send some update emails. Please try again later.')

        except Exception as e:
            # Handle exceptions, e.g., log the error
            print(str(e))
            messages.error(request, 'An error occurred while sending the update emails. Please try again later.')

    send_email_action.short_description = 'Send Update Email to Driver'

    def pdf_download(self, request, queryset):
        # Create a PDF document
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="logbook_report.pdf"'

        # Create a canvas and generate the PDF content
        p = canvas.Canvas(response)
        for obj in queryset:
            self.generate_pdf(p, obj)
            p.showPage()
        p.save()

        return response

    def generate_pdf(self, p, obj):
        # Customize the PDF content based on the logbook report object
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, 750, f"Report for car {obj.car}, - reported: {obj.date_of_fault}")

        p.setFont("Helvetica", 12)
        table_data = [
            ['Field', 'Value'],
            ['Grade', obj.Grade],
            ['Driver Name', obj.driver_name],
            ['Driver Email', obj.driver_email],
            ['Location at Time of Fault', obj.location_at_time_of_fault],
            ['Time of Fault', obj.time_of_fault],
            ['Defect Keyword', obj.defect_keyword],
            ['Defect Details', obj.defect_details],
            ['Ref Number', obj.ref_number],
            ['Report Read', obj.report_read],
            ['Work Order Created', obj.work_order_created],
            ['Driver Emailed', obj.driver_emailed],
            ['Work Order Closed', obj.work_order_closed],
            ['Work Order Number', obj.work_order_number],
            ['Depot Feedback', obj.Depot_feedback],
        ]

        p.setFillColor(colors.black)
        row_height = 20
        for i, row in enumerate(table_data):
            for j, cell in enumerate(row):
                x = 100 + j * 200
                y = 700 - (i + 1) * row_height
                p.drawString(x, y, str(cell))

        p.line(100, 670, 500, 670)


