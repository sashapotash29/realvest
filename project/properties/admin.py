from django.contrib import admin
from properties.models import Properties, Comment, UserProp
# Register your models here.
admin.site.register(Properties)
admin.site.register(Comment)
admin.site.register(UserProp)