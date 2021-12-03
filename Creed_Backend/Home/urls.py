from . import views
from django.urls import path

urlpatterns = [
    path('join_us/', views.join_us, name='joinus'),
    path('', views.index, name='home'),
    path('about_us/', views.about, name='about_us'),
]
