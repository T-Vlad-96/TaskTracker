from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from .models import Task, Tag


class TagListView(ListView):
    model = Tag
    template_name = "tracker/tags.html"


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("tracker:home")

class HomeListView(ListView):
    model = Task
    template_name = "tracker/home.html"

