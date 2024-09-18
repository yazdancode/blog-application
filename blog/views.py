from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm
from blog.models import Post


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    return render(request, "blog/detail.html", {"post": post, "form": form})
