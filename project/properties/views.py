from django.shortcuts import render

# Create your views here.

def show_all(request):
	return render(request, 'properties/properties.html')

def single(request, id):
	return render(request, 'properties/singleProperty.html')

def edit_prop(request, id):
	pass


########### single time use to be hit from Flask app ########

def seed_prop(request):
	pass

