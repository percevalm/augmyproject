from django.db import models

# Create your models here.
class Calendar(models.Model):
	
	Event_Type = models.ForeignKey('EventType', on_delete=models.CASCADE, related_name='type')
	title = models.TextField(max_length=2000)
	description = models.TextField(max_length=2000)
	speaker = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	urllink = models.URLField(max_length=200,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title +' | '+ str (self.description) +' | '+ str (self.speaker) + ' | '+ str (self.location) +' | '+ str (self.start_date) +' | '+ str (self.end_date) + ' | '+ str (self.urllink) 
	class Meta:
		verbose_name_plural = "Calendar"
class EventType(models.Model):

	name = models.CharField(max_length=200)
	description = models.TextField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Event type"
	def __str__(self):
			return self.name 