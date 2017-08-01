
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.forms import (
	UserCreationForm, 
	UserChangeForm, 
	AuthenticationForm, 
	PasswordChangeForm
	)
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.forms.models import model_to_dict
# from django.urls import reverse
from user.forms import RegistrationForm, EditAccountForm

# Create your views here.


# def login(request):
# 	params= {}
# 	return render(request, 'realtor/login.html', params)

#############################
######## route /home #####

def home(request):
	if request.method == "POST":
		print('==============', request.user)
		form = AuthenticationForm(request.POST)
		username =request.POST['username']
		password = request.POST['password']
		user = authenticate(request=request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			args = {'user':request.user, 'properties': Properties.properties.all()}

			return render(request, 'user/home.html', args)
		else:
			error = 'The Username and Password you have provided was not correct.'
			args = {'lform':form,'lError_message':error, 'rform': RegistrationForm()}
			return render(request, 'user/login.html',args)
	
	if request.method == "GET":
		if request.user.is_authenticated():
			args = {'user':request.user, 'properties': Properties.properties.all() }
			return render(request, 'user/home.html', args)
		else:
			error = 'You must first sign in to view that page. If you do not have an account then you must sign up.'
			args = {'rform':RegistrationForm(),'message':error, 'lform':AuthenticationForm()}
			return render(request, 'user/login.html', args)

#############################
######## route /register #####

def register(request):
	if request.method == "POST":
		# print(dir(request))
		form = RegistrationForm(request.POST)
		print(form)
		if form.is_valid():
			print('valid')
			form.save()
			message = "You have successfully created an account. Login to Get Investing!"
			args = {'rform':RegistrationForm(),
					 'lform':AuthenticationForm(),
					  'message':message
					  }
			return render(request, 'user/login.html', args)
		else:
			print('not valid')
			error = 'The Username you have provided is already taken.'
			args = {'rform':RegistrationForm(),'message':error, 'lform':AuthenticationForm()}
			return render(request, 'user/login.html', args)

	else:
		print('wrong request sent')

