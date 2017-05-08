from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.landing_page, name="login"),
	url(r'^register$', views.register, name="signup"),
	url(r'^login$', views.home, name="home"),
	# url(r'^login$', views.login, name="home"),


]