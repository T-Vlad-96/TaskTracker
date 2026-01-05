from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    SwitchTaskStatusView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
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
    ),

    path(
        "switch_task_status/<int:pk>/",
        SwitchTaskStatusView.as_view(),
        name="switch_task_status"
    )
]

app_name = "tracker"
