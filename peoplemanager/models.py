from django.db import models
from archivesuploads.models import Archivesuploads # added as per blog post
from multiselectfield import MultiSelectField


# Create your models here.
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your models here.

class PeopleDetail(models.Model):

	firstnames = models.CharField(max_length=200)
	surname	= models.CharField(max_length=200)
	bio = models.TextField(max_length=20000,null=True,blank=True)
	email = models.EmailField(max_length=200,null = True,blank=True)
	website = models.URLField(max_length=200,null=True, blank=True)
	#staffdetail = models.ForeignKey(StaffDetail)

	headshot = models.ImageField(upload_to='personimage',default='personimage/default.png')

	class Meta:
		verbose_name_plural = "Person details"

	def __str__(self):
		return self.firstnames +	' , '  + str (self.surname)

		# + str (self.bio)+ ' | '  + str (self.email) + ' | ' + str(self.website) + '|'
def image_tag(self):
       return mark_safe('<img src="/personimage/" width="174" height="262" />'  (self.headshot_image))

image_tag.short_description = 'Image'


class StaffDetail(models.Model):
	person_id = models.ForeignKey(PeopleDetail, on_delete=models.CASCADE,related_name='person', null=True, blank=True)
	#category = models.CharField(max_length=200)
	CS = 'Core Staff'
	RAF = 'Research Associates And Fellows'
	PDRF = 'Postdoctoral Research Fellow'
	SC='Steering Committee'
	SAC='Scientific Advisory Committee'

	STAFF_CATEGORY_CHOICES = (
		('CS','Core Staff'),
		('RAF','Research Associates And Fellows'),
		('PDRF','Postdoctoral Research Fellow'),
		('SC','Steering Committee'),
		('SUSAC','Scientific Advisory Committee'),

		)
	category = MultiSelectField(choices = STAFF_CATEGORY_CHOICES)
	#category2 = models.ForeignKey(StaffCategories, on_delete=models.CASCADE,related_name=staffcategories2,null=True,blank=True)
	BCom = 'BCom'
	BTech = 'BTech'
	BSc = 'BSc'
	Hons = 'Hons'
	MTech = 'MTech'
	MBA = 'MBA'
	MSc = 'MSc'
	PhD = 'PhD'
	DEGREE_CHOICES = (
		('BCom','BCom'),
		('BTech','BTech'),
		('BSc','BSc'),
		('Hons','Hons'),
		('MTech','MTech'),
		('MBA','MBA'),
		('MSc','MSc'),
		('PhD','PhD'),
		)
	qualification = models.CharField(max_length = 8, null=True, blank=True, choices = DEGREE_CHOICES)
	job_title = models.CharField(max_length=500)
	job_description =models.TextField(max_length=20000,null=True, blank=True)
	research_theme =models.TextField(max_length=200000,null=True, blank=True)
	appointment_date =models.DateField(max_length=200)
	termination_date =models.DateField(max_length=200,null=True,blank=True)
	is_active =models.BooleanField(default=True)
	def __str__(self):
		return self.job_title + ' | '  + ' | '  + str (self.category) + ' | '  + str (self.job_title) + ' | '  + str (self.job_description) + ' | '  + str (self.appointment_date) + ' | '  + str (self.termination_date) + ' | '  + str (self.is_active) + ' | '


class StudentDetail(models.Model):
	person_id= models.ForeignKey(PeopleDetail, on_delete=models.CASCADE,related_name='supervisor', null=True, blank=True)

	supervisor = models.CharField(max_length=500, null=True, blank=True)
	supervisor_additional = models.CharField(max_length=500, null=True, blank=True)
	institution = models.CharField(max_length=500)
	department = models.CharField(max_length=500, null=True, blank=True)
	thesis_title =models.TextField(max_length=10000)
	MSc = 'MSc'
	PhD = 'PhD'
	ERF = 'ERF'
	Hons ='Hons'
	DEGREE_CHOICES = (
		('MSc','MSc'),
		('PhD','PhD'),
		('ERF','ERF'),
		('Hons','Hons'),
		)
	degree = models.CharField(max_length = 8, choices = DEGREE_CHOICES)

	REGISTRATION_CHOICES = (
		('No','No'),
		('Yes','Yes'),
		)
	currently_registered = models.CharField(max_length = 3, choices = REGISTRATION_CHOICES)
	start_date = models.DateField()
	graduation_date = models.DateField(max_length=200,null=True,blank=True)
	abstract = models.TextField(max_length=20000,null=True, blank=True)
	archivesupload_id =models.CharField(max_length =100,null=True, blank=True)
	class Meta:
		verbose_name_plural = "Student details"

	#def __str__(self):
		#	return self.supervisor + ' | '   + str (self.supervisor_additional) + ' | '  + str (self.institution) + ' | '  + str (self.department) + ' | '  + str (self.thesis_title) + ' | '
