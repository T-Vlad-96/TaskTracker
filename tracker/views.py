from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    View,
)

from .forms import TaskForm
from .models import Task, Tag


class TagListView(ListView):
    model = Tag
    template_name = "tracker/tags.html"


class TagCreateView(CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tracker:tags")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tracker:home")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tracker:tags")
    template_name = "tracker/tag_delete_confirm.html"


class TaskListView(ListView):
    model = Task
    template_name = "tracker/home.html"
    ordering = ["is_done", "created"]


class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("tracker:home")
    form_class = TaskForm


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("tracker:home")
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tracker:home")
    template_name = "tracker/task_delete_confirm.html"


class SwitchTaskStatusView(View):

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("tracker:home")
