from django.contrib.sitemaps import Sitemap

from blog.models import Category, Post


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.active)

    @staticmethod
    def lastmod(obj):
        return obj.created_at
