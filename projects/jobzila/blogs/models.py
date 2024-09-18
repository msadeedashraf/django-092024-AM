from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    slug = models.SlugField()
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default="Sadeed", max_length=40)
    banner = models.ImageField(default="", blank="True")

    def __str__(self):
        return self.title
