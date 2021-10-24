from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('index',  views.index, name='index'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('main', views.main_page, name='main')
]