from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'content', 'body']
