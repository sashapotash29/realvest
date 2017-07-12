
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


def login(request):
	params= {}
	return render(request, 'realtor/login.html', params)