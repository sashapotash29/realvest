from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.forms.models import model_to_dict
from properties.models import Properties
# Create your views here.

#############################
######## route / #####

def landing_page(request):
	if request.method == "GET":
		print(request.body)
		logout(request)
		# print(request.GET)
		args = {'rform':RegistrationForm(), 'lform':AuthenticationForm()}
		return render(request, 'user/login.html', args)
	elif request.method == "POST":  ### finsih after building user signup ###
		prov_username = request.form['existUsername']
		print('request')
	else:
		return('Error')

#############################
######## route /login #####

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
			args = {'user':request.user}
			return render(request, 'user/home.html', args)
		else:
			error = 'The Username and Password you have provided was not correct.'
			args = {'lform':form,'lError_message':error, 'rform': RegistrationForm()}
			return render(request, 'user/login.html',args)
	
	if request.method == "GET":
		if request.user:
			args = {'user':request.user}
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

#################################
######## route /account  #####

def account_private(request):
	# print(request.session)
	# print(dir(request))
	form = UserChangeForm
	args = {'user': request.user, 'form':form}
	# print(args)
	return render(request, 'user/personalPage.html', args)

######## route /account/edit  #####

def account_edit(request):
	if reqiest.method == 'POST': 
		form = UserChangeForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = UserChangeForm(instance=request.user)
		args = {'form':form}
		return render(request, 'user/personlPage.html',)