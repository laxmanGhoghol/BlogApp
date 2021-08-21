from django.urls import path
from . import views
from .views import (
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostListView,
    PostSearchView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("blog/search/", PostSearchView.as_view(), name="post-search"),
    path("about/", views.About, name="blog-about"),
]
