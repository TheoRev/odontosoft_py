from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Patient


def show_all_patients(request):
    patients = Patient.objects.order_by('id')
    template = loader.get_template('patient/index.html')
    context = {
        'patients': patients
    }
    return HttpResponse(template.render(context, request))
