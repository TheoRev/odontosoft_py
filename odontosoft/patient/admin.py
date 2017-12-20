from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class AdminPatient(admin.ModelAdmin):
    list_display = ('nomApe',) 
    list_filter = ('nomApe',)
