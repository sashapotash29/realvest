import json

from .seeder import seed_prop_to_db
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def show_all(request):
	return render(request, 'properties/properties.html')

def single(request, id):
	return render(request, 'properties/singleProperty.html')

def edit_prop(request, id):
	pass


########### Single time use to be hit from seed.py outside 
########### Django project directory 

@csrf_exempt
def seed_prop(request):
	if request.method == "POST":
		data=request.body.decode()
		body=json.loads(data)
		# print(dir(request))
		print(body['result'][0])
		seed_prop_to_db(body['result'][0])
		return HttpResponse('good')
