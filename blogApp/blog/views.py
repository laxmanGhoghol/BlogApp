from django.shortcuts import render
from django.http import request
from .models import Post


def Home(request):
    posts = Post.objects.all()
    context = {"posts": posts, 'title': "Home"}
    return render(request, "blog/home.html", context)


def About(request):
    return render(request, "blog/about.html")

