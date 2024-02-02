from clinic.models import Clinic, Team, Area, Blog, Services
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, TemplateView


class ClinicListView(ListView):
    model = Clinic


class MainView(TemplateView):
    template_name = 'clinic/main.html'


class TeamListView(ListView):
    model = Team


class AreaListView(ListView):
    model = Area


class AreaDetailView(DetailView):
    model = Area


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


class ServicesListView(ListView):
    model = Services
