from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("posts", views.posts, name="post"),
    path("posts/<slug:slug>", views.post_details, name="post_detail_page")
]
