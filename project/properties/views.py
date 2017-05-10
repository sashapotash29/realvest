from django.shortcuts import render

# Create your views here.

def show_all(request):
	return render(request, 'properties.all.html')

def single(request, id):
	return render(request, 'properties/singleProperty.html')

def seed_prop(request):
	pass