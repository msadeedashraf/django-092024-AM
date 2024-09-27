from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.jobs_list, name="joblist"),
]
