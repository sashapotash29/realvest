from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.forms.models import model_to_dict
from properties.models import Properties
# Create your views here.


######## route / #####

def landing_page(request):
	if request.method == "GET":
		print(request.body)
		# print(request.GET)
		args = {'rform':RegistrationForm(), 'lform':AuthenticationForm()}
		return render(request, 'user/login.html', args)
	elif request.method == "POST":  ### finsih after building user signup ###
		prov_username = request.form['existUsername']
		print('request')
	else:
		return('Error')

######## route /login #####

def home(request):
	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		username =request.POST['username']
		password = request.POST['password']
		user = authenticate(request=request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return render(request, 'user/home.html')
		else:
			error = 'The Username and Password you have provided was not correct.'
			args = {'lform':form,'lError_message':error, 'rform': RegistrationForm()}
			return render(request, 'user/login.html',args)

######## route /register #####

def register(request):
	if request.method == "POST":
		# print(dir(request))
		form = RegistrationForm(request.POST)
		print(form)
		if form.is_valid():
			print('valid')
			form.save()
			return render(request, 'user/home.html')
		else:
			print('not valid')
			form = RegistrationForm()
			error = 'The Username you have provided is already taken.'
			args = {'rform':form,'rError_message':error, 'lform':AuthenticationForm()}
			return render(request, 'user/login.html', args)

	else:
		print('wrong request sent')
