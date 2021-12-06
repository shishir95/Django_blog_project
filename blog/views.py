from datetime import datetime

from django.shortcuts import render

# Create your views here.
from blog.models import Data


def home(request):
    model1 = Data.objects.all()

    return render(request, 'index.html', {'models': model1})


def single(request):
    return render(request, 'single.html')


def blog(request):
    return render(request, 'blog.html')
