from django.urls import path
from .views import (
    HomeListView,
    TagListView,
    TagUpdateView,
)

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path(
        "tags/update/<int:pk>/",
        TagUpdateView.as_view(),
        name="tag_update"
    )
]

app_name = "tracker"
