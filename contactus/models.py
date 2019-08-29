from django.db import models
from djgeojson.fields import PointField

# Create your models here.
class Generalenquiries(models.Model):
	
	contact_person= models.CharField(max_length=200, null=True, blank=True)
	contact_email = models.EmailField(max_length=200, null=True, blank=True)
	contact_telephone = models.CharField(max_length=200, null=True, blank=True)
	contact_fax = models.CharField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "General Enquiries"

	def __str__(self):
			return self.contact_person + ' | '  + str (self.contact_email) + ' | '  + str (self.contact_telephone) + ' | '  + str (self.contact_fax)

class Physicaladdress(models.Model):
	
	physical_address= models.TextField(max_length=2000, null=True, blank=True)
	class Meta:
		verbose_name_plural = "Physical Address"

		def __str__(self):
			return self.physical_address + ' | '

class Postaladdress(models.Model):
	
	postal_address= models.TextField(max_length=2000, null=True, blank=True)
	class Meta:
		verbose_name_plural = "Postal Address"
		def __str__(self):
			return self.postal_address + ' | '


class Place(models.Model): # model for sacema locations
	name = models.CharField(max_length=200)
	location = PointField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Sacema Locations"

	def __str__(self):
		return self.name
