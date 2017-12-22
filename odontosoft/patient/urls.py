from django.urls import path
from . import views

urlpatterns = [
    path('patients', views.show_all_patients),
]
