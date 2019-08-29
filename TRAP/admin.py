from django.contrib import admin

from .models import Tsetse
from import_export.admin import ImportExportModelAdmin
from TRAP.resources import TsetseResource
# Register your models here.


class TsetseAdmin(ImportExportModelAdmin):
	list_display = [f.name for f in Tsetse._meta.fields]# this code loops all columns and displays all columns in django admin
	#list_display = ('caseno2','vpn','volume','page','number_on_page','capture_day_of_month','capture_month_year
	list_filter = ['cy','cm','cd']
	ordering = ['pg']

	
	resource_class = TsetseResource #Configure the resource class

admin.site.register(Tsetse,TsetseAdmin)

