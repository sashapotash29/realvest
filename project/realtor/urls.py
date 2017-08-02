from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	# url(r'^login$', views.login, name="realtor_login"),
	url(r'^register$', views.register, name="register"),
	url(r'^home$', views.home, name="home"),
]
