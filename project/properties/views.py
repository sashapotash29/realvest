# Python Library Imports
import json

# Django Imports
from django.contrib.auth.decorators import login_required
from .seeder import seed_prop_to_db
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Model Imports
from properties.models import Properties
# Create your views here.

@login_required
def show_all(request):
	return render(request, 'properties/properties.html')


def deliver_props(request):
	result = Properties.properties.all()
	prop_list = []
	# Necessary to turn QuerySet object into a serializable into a JSON object
	for prop in result: 
		dict_prop = prop.jsonify()
		prop_list.append(dict_prop)
	return JsonResponse({"result": prop_list})


@login_required
def single(request, id):
	return render(request, 'properties/singleProperty.html')

@login_required
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
