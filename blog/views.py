from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
from blog.models import Post, Category


def detail(request,category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=slug)
        else:
            form = CommentForm()
    return render(request, "blog/detail.html", {"post": post, "form": form})

def category(request,slug):
    categorys = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category.html', {'category': categorys})
    

