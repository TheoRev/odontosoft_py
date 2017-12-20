from django.shortcuts import render
from django.template import loader
from django.shortcuts import render

from .models import Patient


def show_all_patients(request):
    patients = Patient.objects.order_by('id')
