from django.shortcuts import render

# Create your views here.

def index(requests):
	# data = blogs.objects.all()
	# print(data)
	return render(requests, 'index.html', {})