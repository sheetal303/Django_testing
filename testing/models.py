from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse("testing:post_detail", args=[self.slug])

    def __str__(self):
        return self.title