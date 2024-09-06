# django-092024-AM

>py --version

>pip install pipenv

create a project folder 

>mkdir hello-world
>cd hello-world

>py -m venv .venv

Activate the env
>.\.venv\Scripts\activate

>(.venv) PS D:\hello-world> py -m pip install Django

To create the django project
>django-admin startproject helloworld

>cd helloworld
>py .\manage.py runserver 8001

create views.py file with the following code

from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Welcome to CBC!")


def about(request):
    return HttpResponse("This is our about page text")


update the urls.py file with the following changes

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage),
    path("about/", views.about),
]


