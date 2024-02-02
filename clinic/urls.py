from django.urls import path
from clinic.apps import ClinicConfig
from clinic.views import (ClinicListView, MainView, TeamListView, AreaListView, AreaDetailView, BlogListView,
                          BlogDetailView, BlogDeleteView, ServicesListView)


app_name = ClinicConfig.name

urlpatterns = [
    path('', ClinicListView.as_view(), name='clinic_list'),
    path('main/', MainView.as_view(), name='main'),
    path('team/', TeamListView.as_view(), name='team_list'),
    path('area/', AreaListView.as_view(), name='area_list'),
    path('area/detail/<int:pk>/', AreaDetailView.as_view(), name='area_view'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('services/', ServicesListView.as_view(), name='services_list'),
]
