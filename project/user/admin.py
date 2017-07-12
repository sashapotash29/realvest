from django.contrib import admin
from user.models import UserProfile, DirectGroup
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(DirectGroup)
# MAKE SURE TO REGISTER YOUR NEW APP

admin.site.site_header = 'RealVest Admin'



