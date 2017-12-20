from __future__ import unicode_literals
from django.db import models


class Patient(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    dateInit = models.DateField(auto_now=True)
    nomApe = models.CharField(max_length=200, blank=False, null=False)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    dateNac = models.DateField()
    address = models.CharField(max_length=200)
    ocupation = models.CharField(max_length=100, blank=False, null=False)
    telCel = models.CharField(max_length=12)
    alergies = models.CharField(max_length=150)
    operations = models.CharField(max_length=150)
    diabettes = models.BooleanField()
    hipertension = models.BooleanField()
    others = models.CharField(max_length=120)
    treatMedics = models.CharField(max_length=120)
    state = models.BooleanField(default=True)
