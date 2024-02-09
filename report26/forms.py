from .models import report_26
from django import forms
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class ReportForm26(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(ReportForm26, self).__init__(*args, **kwargs)
        if request and request.user.is_authenticated:
            self.fields['driver_name'].initial = request.user.username
            self.fields['driver_email'].initial = request.user.email

        # Set initial values for time_of_fault and date_of_fault
        self.fields['time_of_fault'].initial = datetime.now().strftime('%H:%M')
        self.fields['date_of_fault'].initial = datetime.now().strftime('%Y-%m-%d')

    class Meta:
        model = report_26
        fields = (
            'ref_number',
            'Grade',
            'driver_name',
            'driver_email',
            'car',
            'location_at_time_of_fault',
            'time_of_fault',
            'date_of_fault',
            'defect_keyword',
            'defect_details',
        )

        widgets = {
            'date_of_fault': DateInput(),
            'time_of_fault': forms.TimeInput(attrs={'type': 'time'}),
            'defect_details': forms.Textarea(attrs={'placeholder': 'Please provide a full description of the issue to be raised'}),
            'ref_number': forms.HiddenInput(),
        }


class UpdateForm26(forms.ModelForm):
    class Meta:
        model = report_26
        fields = ('driver_email', 'car', 'Depot_feedback', 'ref_number', 'date_of_fault', 'defect_details')