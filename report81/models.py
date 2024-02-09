from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class report_81(models.Model):
    OPTIONS = (
        ('Brake Issue', 'Brake Issue'),
        ('main engine', 'main engine'),
        ('gen engine', 'gen engine'),
        ('EDC fault', 'EDC fault'),
        ('TDC fault', 'TDC fault'),
        ('bad oil level', 'bad oil level'),
        ('low HYDRO oil', 'low HYDRO oil'),
        ('low coolant', 'low coolant'),
        ('door', 'door'),
        ('wiper', 'wiper'),
        ('radio', 'radio'),
        ('wheel flats', 'wheel flats'),
        ('HVAC', 'HVAC'),
        ('Heating', 'Heating'),
        ('caws', 'caws'),
        ('headlamps', 'headlamps'),
        ('mmi', 'mmi'),
        ('Cab Seals', 'Cab Seals'),
        ('Window', 'Window'),
        ('Internal Lights', 'Internal Lights'),
        ('External Lights', 'External Lights'),
        ('Saloon Issues', 'Saloon Issues'),
        ('Fuel Issues', 'Fuel Issues'),
    )

    CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    Grade = models.CharField(max_length=25, default='Driver')
    driver_name = models.CharField(max_length=50)
    driver_email = models.EmailField(blank=True)  # blank =  make optional
    car = models.CharField(max_length=50, default='81')
    location_at_time_of_fault = models.TextField(max_length=60)
    time_of_fault = models.TimeField(null=True, blank=True)
    date_of_fault = models.TextField()
    defect_keyword = models.TextField(choices=OPTIONS, default='', help_text='(By selecting a keyword, this will later help to search and identify problematic trends on a unit)', blank=False)
    defect_details = models.TextField(blank=False, default='')
    ref_number = models.IntegerField(blank=True, null=True)
    status_changed = models.BooleanField(default=False) #15
    
    # admin
    report_read = models.BooleanField(default=False)
    work_order_created = models.BooleanField(default=False)
    driver_emailed = models.BooleanField(default=True)
    work_order_closed = models.BooleanField(default=False)
    work_order_number = models.IntegerField(blank=True, null=True)
    Depot_feedback = models.TextField(max_length=300, default='Copy SAP longtext here')
    
    # broken seal info to be added
    # issue_required_second_person_in_cab = models.CharField(max_length=3, choices=CHOICES, default='no')
    # second_person = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:        
        ordering = ['date_of_fault']