from django.shortcuts import render
from django.views.generic import ListView
from .models import Lesson

class MainSite(ListView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'schoolnotes/index.html'
