from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

class PostMessageView(View):

	def get(self, request, *args):
		print(dir(request))
		return JsonResponse({'response':'hello'})

	def post(self, request, *args):
		pass



