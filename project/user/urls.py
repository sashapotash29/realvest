from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

urlpatterns = [
	url(r'^$', views.landing_page, name="login"),
	url(r'^home$', views.home, name="home"),
	url(r'^login$', views.login, name="login"),
	url(r'^logout$', logout, {'template_name':'user/logout.html'}),
	url(r'^register$', views.register, name="register"),
	url(r'^account$', views.account_private, name="private_account"),
	url(r'^account/edit$', views.account_edit, name="edit_account"),


]