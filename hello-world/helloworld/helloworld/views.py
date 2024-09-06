"""
# to test without pages
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Welcome to CBC!")


def about(request):
    return HttpResponse("This is our about page text")
"""

from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
