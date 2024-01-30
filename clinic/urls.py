from django.urls import path

from clinic.apps import ClinicConfig
from clinic.views import *

app_name = ClinicConfig.name

urlpatterns = [
    path('', ClinicListView.as_view(), name='clinic_list'),
    path('main/', MainView.as_view(), name='main'),

    path('team/', TeamListView.as_view(), name='team_list'),

    path('area/', AreaListView.as_view(), name='area_list'),
    path('area/detail/<int:pk>/', AreaDetailView.as_view(), name='area_view'),

    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
