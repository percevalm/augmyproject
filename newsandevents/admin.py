from django.contrib import admin
from .models import Newsletters, News, Event, Opportunity

# Register your models here.

class NewslettersAdmin(admin.ModelAdmin):
	list_display = ('id','title','newsletter_date','newsletter_number','file','created_at') #
	ordering =	['newsletter_date']
	list_filter =['newsletter_date']
	list_per_page = 15

admin.site.register(Newsletters, NewslettersAdmin)


class NewsAdmin(admin.ModelAdmin):
	list_display = ('id','title','news','url','news_date') #
	ordering =	['news_date']
	#list_filter =['created_at']
	list_per_page = 15

admin.site.register(News, NewsAdmin)


class EventAdmin(admin.ModelAdmin):
	list_display = ('id','title','event','url','event_date') #
	ordering =	['event_date']
	#list_filter =['created_at']
	list_per_page = 15

admin.site.register(Event, EventAdmin)


class OpportunityAdmin(admin.ModelAdmin):
	list_display = ('id','title','opportunity','url','opportunity_date') #
	ordering =	['opportunity_date']
	#list_filter =['created_at']
	list_per_page = 15

admin.site.register(Opportunity, OpportunityAdmin)
