from django.shortcuts import render
from blog.models import Post


def frontpage(request):
    posts = Post.objects.all()

    return render(request, "base/frontpage.html", {"posts": posts})


def about(request):
    return render(request, "base/about.html")
