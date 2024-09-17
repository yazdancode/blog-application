from django.urls import path
from base.views import frontpage


urlpatterns = [
	path('base/', frontpage, name='frontpage')
]