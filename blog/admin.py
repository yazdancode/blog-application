from django.contrib import admin
from blog.models import Post, Category, Comments


class CommentItemInline(admin.TabularInline):
    model = Comments
    raw_id_fields = ["post"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "category", "created_at", "status"]
    search_fields = ["title", "content", "body"]
    list_filter = ["category", "created_at", "status"]
    inlines = [CommentItemInline]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["name", "post", "created_at"]
