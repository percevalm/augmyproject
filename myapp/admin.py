import csv
import datetime
from django.contrib import admin
from .models import Intbursary
from django.http import HttpResponse
#from django.core.urlresolvers import reverse
from django.urls import reverse
from import_export.admin import ImportExportModelAdmin
from myapp.resources import IntbursaryResource
############################### code to export csv #####################################################################
"""
def export_to_csv (modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response [ 'Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	#write the header row
	writer.writerow([field.verbose_name for field in fields])
	#write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
			writer.writerow(data_row)
	return response
export_to_csv.short_description = 'Export to CSV'

def order_detail(obj):
	return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail',
													args=[obj.id]))
order_detail.allow_tags = True

def order_pdf(obj):
	return '<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf',
													args=[obj.id]))
order_pdf.allow_tags = True
order_pdf.short_description ='PDF Bill'

class IntbursaryItemInLine(admin.TabularInline):
	model = Intbursary
	raw_id_fields = ['product']
"""
#################################################code to export csv ###########################################

# Register your models here.

#class IntbursaryAdmin(admin.ModelAdmin): # the below code willl customise the admin panel (Searching, Filters and display of column headings)

class IntbursaryAdmin(ImportExportModelAdmin):
	list_display = ('id','surname','first_name','id_number','nationality','gender','race','email','telephone_number','proposed_degree','created_at')
	list_filter =('proposed_degree','gender','created_at')
	search_fields =('surname','first_name')
	list_per_page =15
	date_hierarchy = 'created_at'
	

	resource_class = IntbursaryResource #Configure the resource class


admin.site.register(Intbursary,IntbursaryAdmin)
