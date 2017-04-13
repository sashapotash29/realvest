from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	url(r'^$', views.login_page, name="login"),
	url(r'^register$', views.register, name="signup"),


]