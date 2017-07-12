from django.conf.urls import url
from .views import PostMessageView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
<<<<<<< HEAD
	url(r'^post/([0-9])$', login_required(PostMessageView.as_view()), name="post_message"),
	url(r'^load/([0-9])$', PostMessageView.as_view(), name="load_conversation"), #Remember to add login_required restiction!!
=======
	url(r'^post/([0-9]{12})$', login_required(PostMessageView.as_view()), name="post_message"),
	url(r'^load/([0-9]{12})$', login_required(PostMessageView.as_view()), name="load_conversation"),
>>>>>>> a2bb234a63e163f4d2ac439a3b59c663ed4b6e51
]