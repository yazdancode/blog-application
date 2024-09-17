from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    content = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
