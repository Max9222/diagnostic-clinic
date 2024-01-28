from django.urls import path

from clinic.apps import ClinicConfig
from clinic.views import ClinicListView

app_name = ClinicConfig.name

urlpatterns = [
    path('', ClinicListView.as_view(), name='clinic_list')
]
