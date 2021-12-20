from os import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting_page"),
    path("posts", views.AllPostView.as_view(), name="post"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_detail_page"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later"),

]
