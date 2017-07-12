from django.contrib import admin
from realtor.models import Realtor




# Register your models here.



admin.site.register(Realtor)
# MAKE SURE TO REGISTER YOUR NEW APP

admin.site.site_header = 'RealVest Admin'