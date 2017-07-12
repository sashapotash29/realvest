from django.contrib import admin
from properties.models import Properties, Comment, Investment
# Register your models here.

#### Customizing Admin Portal

class PropertiesAdmin(admin.ModelAdmin):

	### adding columns
	list_display = ('address','city','state','zipcode', 'status')
	def property_info(self, obj):
		return obj


	### changes order of properties display	
	def get_queryset(self, request):                                   # method inherited from admin.ModelAdmin class
		queryset = super(PropertiesAdmin, self).get_queryset(request)  # uses method functionality from inherited class
		return queryset.order_by('city')                               # admin page currently sorting by city

admin.site.register(Properties, PropertiesAdmin)
admin.site.register(Comment)
admin.site.register(Investment)
