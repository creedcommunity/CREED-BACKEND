from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Blog.Category", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    like = models.IntegerField(default=0)
    tital = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="static/post/images")
    yt_link = models.URLField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.tital


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE,
                               related_name='Author')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    text = models.CharField(max_length=400, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
