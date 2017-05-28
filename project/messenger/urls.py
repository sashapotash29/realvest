from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^load$', views.load_conversation, name="load_message"),
]
