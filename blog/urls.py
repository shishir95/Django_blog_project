from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('single', views.single, name='single'),
    path('blog', views.blog, name='blog')
]