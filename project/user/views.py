from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import RegistrationForm
from django.forms.models import model_to_dict

# Create your views here.

# @login_required
# def my_view(request):

def login_page(request):
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


def home(request):
	if request.method == "POST":
		form = AuthenticationForm(request.GET)
		print(form)
		if form.is_valid():
			return render(request, 'user/home.html')

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
			args = {'rform':form,'rError_message':error}
			return render(request, 'user/login.html', args)



		# print(request.POST['newPassword'])
		# new_username = request.POST['newUsername']
		# check = User.objects.filter(username=new_username)
		# print(check)
		# if len(check)>0:
		# 	error = 'The Username you have provided is already taken.'
		# 	return render(request, 'user/login.html', {'rError_message':error})
		# else:
		# 	user = User(
		# 		username=request.POST['newUsername'],
		# 		password=request.POST['newPassword'],
		# 		first_name=request.POST['newFirstName'],
		# 		last_name=request.POST['newLastName']
		# 		)
		# 	user.save()
		# 	return render(request, 'user/home.html')

	else:
		print('wrong request sent')
