from django.urls import path
from base.views import frontpage, about, robots_txt


urlpatterns = [
    path("base/", frontpage, name="frontpage"),
    path("about/", about, name="about"),
    path("robots_txt/", robots_txt, name="robots_txt"),
]
