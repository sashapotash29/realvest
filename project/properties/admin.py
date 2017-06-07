from django.contrib import admin
from properties.models import Properties, Comment, UserProp
# Register your models here.

class PropertiesAdmin(admin.ModelAdmin):
	list_display = ('address','city','state','zipcode', 'status')

	def property_info(self, obj):
		return obj





admin.site.register(Properties, PropertiesAdmin)
admin.site.register(Comment)
admin.site.register(UserProp)
# admin.site.register(PropertiesAdmin)
