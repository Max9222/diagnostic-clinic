from django.urls import path

from clinic.apps import ClinicConfig
from clinic.views import ClinicListView, TeamListView

app_name = ClinicConfig.name

urlpatterns = [
    path('', ClinicListView.as_view(), name='clinic_list'),

    path('team/', TeamListView.as_view(), name='team_list'),
]
