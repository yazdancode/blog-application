from django.contrib import admin
from blog.models import Post, Category, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","category", "created_at"]
    search_fields = ['title', 'content', 'body']
    list_filter = ['category', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ['title']
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    
    
