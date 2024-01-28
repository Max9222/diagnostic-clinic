from django.shortcuts import render
from django.views.generic import ListView
from clinic.models import Clinic, Team


class ClinicListView(ListView):
    model = Clinic

class TeamListView(ListView):
    model = Team
