from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("about/", views.AboutView.as_view()),
    path("contact/", views.ContactView.as_view()),
    path("result/<str:task_id>/", views.CheckResult.as_view()),
]
