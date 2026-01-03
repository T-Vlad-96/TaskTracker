from django.shortcuts import render
from django.views.generic import ListView

from .models import Task, Tag


class HomeListView(ListView):
    model = Task
    template_name = "tracker/home.html"


class TagListView(ListView):
    model = Tag
    template_name = "tracker/tags.html"