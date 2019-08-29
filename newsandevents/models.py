from django.db import models

# Create your models here.
class Newsletters(models.Model):

	title = models.CharField(max_length=200, null=True, blank=True)
	newsletter_date = models.DateField(null=True, blank=True)
	newsletter_number = models.CharField(max_length=200, null=True, blank=True)
	file =models.FileField(upload_to='newsletters', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Newsletters"


class News(models.Model):
	title = models.CharField(max_length=2000,null=True,blank=True)
	news = models.TextField(max_length=20000,null=True,blank=True)
	url = models.URLField(max_length=50000,null=True,blank=True)
	news_date = models.DateField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "News"
	def __str__(self):
		return self.title + ' | ' + str (self.news) + ' | ' + str (self.url) + ' | ' + str (self.news_date) + '|' + str (self.created)+ '|'


class Event(models.Model):
	title = models.CharField(max_length=2000,null=True,blank=True)
	event = models.TextField(max_length=20000,null=True,blank=True)
	url = models.URLField(max_length=50000,null=True,blank=True)
	event_date = models.DateField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Event"
	def __str__(self):
		return self.title + ' | ' + str (self.event) + ' | ' + str (self.url) + ' | ' + str (self.event_date) + '|' + str (self.created)+ '|'


class Opportunity(models.Model):
	title = models.CharField(max_length=2000,null=True,blank=True)
	opportunity = models.TextField(max_length=20000,null=True,blank=True)
	url = models.URLField(max_length=50000,null=True,blank=True)
	opportunity_date = models.DateField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Opportunity"
	def __str__(self):
		return self.title + ' | ' + str (self.opportunity) + ' | ' + str (self.url) + ' | ' + str (self.opportunity_date) + '|' + str (self.created)+ '|'
