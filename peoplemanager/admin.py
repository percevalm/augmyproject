from django.contrib import admin

# Register your models here.

from .models import PeopleDetail, StaffDetail, StudentDetail
import datetime
from django.utils.safestring import mark_safe
#""" Register your models here.

class StaffDetailStackedInline(admin.StackedInline): #Tabular inline function and model
	model = StaffDetail
	fields= ('id','category','qualification','job_title','job_description','research_theme','appointment_date','termination_date','is_active', 'person_id') # Fields displayed
	
	extra = 1 # this will display only one inline form for one record in the django admin
	max_num = 1 # this will display a maximum of only one inline forms for two records in the django admin


class StudentDetailStackedInline(admin.StackedInline): # Tabular inline function and model for student details
	model = StudentDetail
	fields = ('supervisor','supervisor_additional','institution','department','thesis_title','degree','currently_registered','start_date','graduation_date','abstract','archivesupload_id','person_id')
	list_filter =['degree']
	ordering = ['id']
	extra = 1
	max_num = 2	# this will display a maximum of only two inline forms for two records in the django admin in the event a student registers for two degrees

class PeopleDetailAdmin(admin.ModelAdmin): # the below code willl customise the admin panel (Searching, Filters and display of column headings)
	list_display = ('id','firstnames','surname','bio','email','website','headshot_image')
	#list_filter =('proposed_degree','gender','created_at')
	search_fields = ['surname','firstnames']
	readonly_fields= ["headshot_image"] # this code will display the title against the uploaded picture from edit page
	ordering = ['id']
	def headshot_image(self, obj): # this code will display uploaded profile picture  based on the pixels of the pic without any edits
		return mark_safe('<img src="{url}" width="174" height="262" />'.format(
			url = obj.headshot.url,
			width=obj.headshot.width,
			height=obj.headshot.height,
			)
	)
		class meta:
			model = PeopleDetail

	inlines =(StaffDetailStackedInline, StudentDetailStackedInline)# inline forms for Staff and sudents




class StudentDetailAdmin(admin.ModelAdmin): # the below code willl customise the admin panel (Searching, Filters and display of column headings)
	list_display = ('id','person_id','supervisor','supervisor_additional','institution','department','thesis_title','degree','currently_registered','start_date','graduation_date','abstract','archivesupload_id')
	list_filter =['degree','currently_registered','graduation_date']
	ordering = ['id']
	list_per_page =25
	#search_fields =('surname','first_name')



class StaffDetailAdmin(admin.ModelAdmin):
	list_display=('id','category','person_id','qualification','job_title','research_theme','job_description','appointment_date','termination_date','is_active')
	list_filter = ['category']
	ordering = ['id']
	list_per_page =25

admin.site.register(PeopleDetail, PeopleDetailAdmin)
admin.site.register(StaffDetail, StaffDetailAdmin)
admin.site.register(StudentDetail, StudentDetailAdmin)
