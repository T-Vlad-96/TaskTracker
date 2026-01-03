from django.urls import path
from .views import HomeListView, TagListView

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags")
]

app_name = "tracker"
