from django.db import models

# Create your models here.
class Archivesuploads(models.Model):
	journal= models.ForeignKey('Interests', on_delete=models.CASCADE, related_name='InterestsType',null=True,blank=True)
	archivetype = models.ForeignKey('Archivetypes', on_delete=models.CASCADE, related_name='ArchiveType',null=True,blank=True)
	name = models.TextField(max_length=200000,null=True,blank=True)
	title = models.TextField(max_length=200000,null=True,blank=True)
	file =models.FileField(upload_to='archives', null=True, blank=True)
	size = models.CharField(max_length=2000,null=True,blank=True)
	url = models.URLField(max_length=50000,null=True,blank=True)
	publication_date = models.DateField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	general_doi = models.TextField(max_length=200000)
	class Meta:
		verbose_name_plural = "Archive uploads"
	def __str__(self):
		return self.name + ' | ' + str (self.title) + ' | ' + str (self.url) + ' | ' + str (self.publication_date) + '|' + str (self.created)+ '|' + str (self.general_doi)+ '|'

	

class Archivetypes(models.Model):
	name = models.CharField(max_length=2000,null=True,blank=True)
	description = models.TextField(max_length=2000,null=True,blank=True)
	class Meta:
		verbose_name_plural = "Archive types"
	def __str__(self):
		return self.name



class Interests(models.Model):
	name = models.CharField(max_length=2000,null=True,blank=True)
	description = models.CharField(max_length=2000,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Interests"
	def __str__(self):
		return self.name
