from django.contrib import admin
from .models import Calendar, EventType
# Register your models here.
#class EventTypeTabularInline(admin.TabularInline): #Tabular inline function and model
#	model = EventType
	#fields= ('id','name','description') # Fields displayed 
	#extra = 1 # this will display only one inline form for one record in the django admin
	#max_num = 1 # this will display a maximum of only one inline forms for two records in the django admin


class CalendarAdmin(admin.ModelAdmin):
	list_display = ('id','title','Event_Type','description','speaker','location','start_date','end_date','urllink')
	search_fields = ['speaker']
	list_filter = ['start_date'] 
	ordering =	['start_date'] #order records in admin by start_date

	

admin.site.register(Calendar, CalendarAdmin)

class EventTypeAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','created')
	ordering = ['id']

admin.site.register(EventType, EventTypeAdmin)

