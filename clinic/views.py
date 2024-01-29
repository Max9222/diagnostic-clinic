from django.shortcuts import render
from django.views.generic import ListView
from clinic.models import Clinic, Team, Area, Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.http import Http404


class ClinicListView(ListView):
    model = Clinic


class TeamListView(ListView):
    model = Team


class AreaListView(ListView):
    model = Area

class AreaDetailView(DetailView):
    model = Area
    permission_required = 'clinic.area_view'



class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('clinic:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('clinic:blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('clinic:blog_list')