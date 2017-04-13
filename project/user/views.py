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
		print(dir(request))
		print(request.META)
		# form = signup_form(request.POST)
		# dic = model_to_dict(form)
		# print(dic)
		# arr=[]
		# for each in form:
		# 	arr.append(each.value())
		# print(arr)
		# print('--------------')
		# print(dir(form))
		# print('--------------')

		# print(type(form.cleaned_data['newUsername']))
		# print(form['newUsername'].value)

		# new_username = request.form['newUsername']
		# result = User.objects.filter(username=new_username)
	elif request.method == "GET":
		print('get request')
