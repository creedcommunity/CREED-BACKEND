from django.contrib import admin
from .models import *


# Register your models here.

class GroupDataAdmin(admin.ModelAdmin):
    list_display = ['category', 'group_name', 'total_members', 'created_at', 'author']
    search_fields = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['author', 'name']
    search_fields = ['name']


admin.site.register(Group_Data, GroupDataAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(category)
# admin.site.register(About_us)
