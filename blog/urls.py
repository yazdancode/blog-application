from django.urls import path
from django.conf.urls.static import static
from blog.views import detail, category, search
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CategorySitemap, PostSitemap
from . import views

sitemaps = {"category": CategorySitemap, "post": PostSitemap}
urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("search/", search, name="search"),
    path("<slug:category_slug>/<slug:slug>/", detail, name="post_detail"),
    path("<slug:slug>/", category, name="category_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
