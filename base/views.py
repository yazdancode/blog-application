from gettext import textdomain

from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def frontpage(request):
    posts = Post.objects.filter(status=Post.active)

    return render(request, "base/frontpage.html", {"posts": posts})


def about(request):
    return render(request, "base/about.html")


def robots_txt(request):
    text = [
        "User-Agent:*",
        "Disallow :/admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
