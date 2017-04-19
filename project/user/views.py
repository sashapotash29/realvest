from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .forms import signup_form
from django.forms.models import model_to_dict

# Create your views here.

# @login_required
# def my_view(request):

def login_page(request):
	if request.method == "GET":
		print(request.body)
		# print(request.GET)
		return render(request, 'user/login.html', {})
	elif request.method == "POST":  ### finsih after building user signup ###
		prov_username = request.form['existUsername']
		print('request')
	else:
		return('Error')


def home(request):
	pass

def register(request):
	if request.method == "POST":
		# print(dir(request))
		print(request.POST['newPassword'])
		new_username = request.POST['newUsername']
		check = User.objects.filter(username=new_username)
		print(check)
		if len(check)>0:
			error = 'The Username you have provided is already taken.'
			return render(request, 'user/login.html', {'rError_message':error})
		else:
			user = User(
				username=request.POST['newUsername'],
				password=request.POST['newPassword'],
				first_name=request.POST['newFirstName'],
				last_name=request.POST['newLastName']
				)
			user.save()
			return render(request, 'user/home.html')

	elif request.method == "GET":
		print('get request')
