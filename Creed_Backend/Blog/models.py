from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    like = models.IntegerField(default=0)
    tital = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="static/post/images")
    yt_link = models.URLField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.tital
