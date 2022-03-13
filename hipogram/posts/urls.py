from django.urls import path

from .views import post_list_view

app_name = "posts"

urlpatterns = [
    path("", post_list_view, name="list"),
]
