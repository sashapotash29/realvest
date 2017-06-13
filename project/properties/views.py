import json

from django.contrib.auth.decorators import login_required
from .seeder import seed_prop_to_db
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def show_all(request):
	return render(request, 'properties/properties.html')

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
