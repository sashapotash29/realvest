from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
# def my_view(request):

def login_page(request):
	print('hitting login')
	return render(request, 'user/login.html', {})
