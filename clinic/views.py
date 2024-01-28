from django.shortcuts import render
from django.views.generic import ListView
from clinic.models import Clinic


class ClinicListView(ListView):
    model = Clinic
