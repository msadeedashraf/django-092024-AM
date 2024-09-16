from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blogs, name="bloglist"),
    path("<slug:slug>", views.blog_page, name="blogdetails"),
]
