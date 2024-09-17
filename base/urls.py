from django.urls import path
from base.views import frontpage, about


urlpatterns = [
    path("base/", frontpage, name="frontpage"),
    path("about/", about, name="about"),
]
