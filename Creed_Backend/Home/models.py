from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group_Data(models.Model):
    link = models.URLField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=300, null=False, blank=False)
    total_members = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class About_us(models.Model):
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_at)
