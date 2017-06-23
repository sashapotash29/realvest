from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^post$', login_required(PostMessageView.as_view(message)), name="post_message"),
	url(r'^load$', login_required(LoadMessageView.as_view()), name="load_conversation"),
]