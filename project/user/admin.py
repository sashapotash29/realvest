from django.contrib import admin
from user.models import UserProfile
# Register your models here.
admin.site.register(UserProfile)

admin.site.site_header = 'RealVest Admin'

