from django.urls import path
from .views import (
    HomeListView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
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
