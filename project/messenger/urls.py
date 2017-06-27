from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^post/([0-9]{12})$', login_required(PostMessageView.as_view(message)), name="post_message"),
	url(r'^load/([0-9]{12})$', login_required(PostMessageView.as_view()), name="load_conversation"),
]