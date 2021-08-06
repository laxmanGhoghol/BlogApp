from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.

def Home(request):
    return HttpResponse('<h1>Blog</h1>')