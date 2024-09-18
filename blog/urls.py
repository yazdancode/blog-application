from django.urls import path
from blog.views import detail


urlpatterns = [
	path('<slug:slug>/', detail, name='post_detail'),
]