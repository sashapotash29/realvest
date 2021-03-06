from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^all$', views.show_all, name="property_list"),
	url(r'^deliprops$', views.deliver_props, name="deliver_properties"),
	url(r'^single/([0-9]{3})', views.single, name="property_single"),
	# Currently Set at 3 because we are dealing in the hundred of properties. In the future, need to change.
	url(r'^single/edit/([0-9]{12})$', views.edit_prop, name="property_edit"),
	url(r'^seed$', views.seed_prop, name="property_seeding"),
]
