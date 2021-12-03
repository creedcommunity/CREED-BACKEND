from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'home/Home.html')


def join_us(request):
    query = Group_Data.objects.all()
    context = {'groups': query}
    return render(request, 'join_us/joinus.html', context)


def about(request):
    query = About_us.objects.all()
    # print(query.text)
    context = {'texts': query}
    return render(request, 'about/about.html', context)
