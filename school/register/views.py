from dataclasses import field
from django.shortcuts import render
from django.urls import reverse_lazy
from register.models import Teacher
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.
def home_views(request):
    return render(request, "home.html")

class ThanksTemplateView(TemplateView):
    template_name ="thank_you.html"


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('register:thanks')


class TeacherListview(ListView):
    model = Teacher
    context_object_name = "teacher_list"

class TeacherDetailview(DetailView):
    model = Teacher    


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('register:teacher_list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('register:teacher_list')

