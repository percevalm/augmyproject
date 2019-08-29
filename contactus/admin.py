from django.contrib import admin
from .models import Generalenquiries, Physicaladdress, Postaladdress, Place
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class GeneralenquiriesAdmin(admin.ModelAdmin):
	list_display = ('id','contact_person','contact_email','contact_telephone','contact_fax','created_at')
	
admin.site.register(Generalenquiries, GeneralenquiriesAdmin)

class PhysicaladdressAdmin(admin.ModelAdmin):
	list_display = ['physical_address']

admin.site.register(Physicaladdress, PhysicaladdressAdmin)

class PostaladdressAdmin(admin.ModelAdmin):
	list_display = ['postal_address']

admin.site.register(Postaladdress, PostaladdressAdmin)
	
admin.site.register(Place, LeafletGeoAdmin)