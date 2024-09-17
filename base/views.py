from django.shortcuts import render


def frontpage(request):
	return render(request, 'base/frontpage.html')


def about(request):
	return  render(request, 'base/about.html')