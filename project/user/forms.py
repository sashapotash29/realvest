from django import forms
from .models import User
# from django.contrib.auth.models import User

class signup_form(forms.Form):
	# newUsername = forms.CharField(max_length=100)
	# newPassword = forms.CharField(max_length=100)
	# newFirstName = forms.CharField(max_length=25)
	# newLastName = forms.CharField(max_length=25)

	class Meta:
		model = User
		fields = ['username','password','newFirstName','newLastName']

	# def __str__(self):
	# 	return self.newUsername

