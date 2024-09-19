from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
from blog.models import Post, Category


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.active)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=slug)

    return render(request, "blog/detail.html", {"post": post, "form": form})


def category(request, slug):
    category_instance = get_object_or_404(Category, slug=slug)
    posts = category_instance.posts.filter(status=Post.active)
    return render(
        request, "blog/category.html", {"category": category_instance, "posts": posts}
    )


def search(request):
    query = request.GET.get("query", "")
    posts = Post.objects.filter(status=Post.active).filter(
        Q(title__icontains=query)
        | Q(content__icontains=query)
        | Q(body__icontains=query)
    )
    return render(request, "blog/search.html", {"posts": posts, "query": query})
