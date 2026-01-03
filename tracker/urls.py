from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TaskCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path(
        "tags/update/<int:pk>/",
        TagUpdateView.as_view(),
        name="tag_update"
    ),
    path(
        "tags/delete/<int:pk>/",
        TagDeleteView.as_view(),
        name="tag_delete"
    )
]

app_name = "tracker"
