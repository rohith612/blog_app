from django.urls import path
from . import views

urlpatterns = [
    path('feedback', views.FeedbackView.as_view(), name="feedback"),
]
