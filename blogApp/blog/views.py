from django.shortcuts import render
from django.http import request
# Create your views here.

def Home(request):
    return render(request, 'blog/home.html')

def About(request):
    return render(request, 'blog/about.html')