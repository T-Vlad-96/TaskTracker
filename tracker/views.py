from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

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


def switch_task_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("tracker:home")
