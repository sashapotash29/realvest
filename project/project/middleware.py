# import re
# from django.conf import settings
# from django.shortcuts import redirect
# print('in middleware.py')


# # EXEMPT_URL = [re.compile(settings.LOGIN_EXEMPT_URL.lstrip('/'))]

# if hasattr(settings, 'LOGIN_EXEMPT_URL'):
# 	EXEMPT_URLS = [re.compile(url) for url in settings.LOGIN_EXEMPT_URL]
# 	# EXEMPT_URL.append(EXEMPTs)


# class LoginRequiredMiddleware:
# 	def __init__(self, get_response):
# 		self.get_response = get_response

# 	def __call__(self, request):
# 		response = self.get_response(request)
# 		return response

# 	def process_view(self, request, view_func, view_args, view_kwargs):
# 		assert hasattr(request, 'user')
# 		path = request.path_info.lstrip('/')
# 		print(request.path_info)
# 		print('in process_view')
# 		# print(dir(request.user))
# 		if not request.user.is_authenticated():
# 			print('step 1')
# 			print(EXEMPT_URLS)
# 			print('path1')
# 			print(path)
# 			# x =[url.match(path) for url in EXEMPT_URL]
# 			# for y in x:
# 			# 	print(y)
# 			# 	print(dir(y))
			
# 			if not any(url.match(path) for url in EXEMPT_URLS):
# 				print('path2')
# 				print(path)
# 				# print(settings.LOGIN_URL)
# 				return redirect(settings.LOGIN_URL)