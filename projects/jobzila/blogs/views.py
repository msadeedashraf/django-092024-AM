from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {"blogs": blogs})


def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog_post.html", {"blog": blog})
