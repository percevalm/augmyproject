from django.db import models
from django.utils import timezone
#from myapp.validation import ContentTypeRestrictedFileField
#from djchoices import ChoiceItem, DjangoChoices

# Create your models here. # these will have column names and column properties
class Intbursary(models.Model):

	surname = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	id_number = models.CharField(max_length=200)


	nationality = models.CharField(max_length=200)
	Black = 'Black'
	White = 'White'
	Indian = 'Indian'
	Colored = 'Colored'
	Other = 'Other'
	RACE_CHOICES = (
		('Black','Black'),
		('White','White'),
		('Indian','Indian'),
		('Colored','Colored'),
		('Other','Other'),
			)
	race = models.CharField(max_length = 7, choices = RACE_CHOICES)
	Male = 'Male'
	Female = 'Female'
	GENDER_CHOICES = (
		('Male','Male'),
		('Female','Female'),
		)

	gender = models.CharField(max_length = 8, choices = GENDER_CHOICES)
	telephone_number = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	FullTime = 'FullTime'
	PartTime = 'PartTime'
	No = 'No'
	EMPLOYED_CHOICES = (
		('FullTime','FullTime'),
		('PartTime','PartTime'),
		('No','No'),
		)

	employed = models.CharField(max_length = 10, choices = EMPLOYED_CHOICES)
	employed_at = models.CharField(max_length=200)

	FullTime = 'FullTime'
	PartTime = 'PartTime'

	STUDY_CHOICES = (
		('FullTime','FullTime'),
		('PartTime','PartTime'),
		)

	full_part_time = models.CharField(max_length = 10, choices = STUDY_CHOICES)

	Yes = 'Yes'
	Yes = 'Yes'

	EMPLOYED_STUDY_CHOICES = (
		('Yes','Yes'),
		('No','No'),
		)

	employed_study = models.CharField(max_length = 3, choices = EMPLOYED_STUDY_CHOICES)

	employed_study_details=models.TextField(max_length=200)
	Msc = 'Msc'
	PhD = 'PhD'
	DEGREE_CHOICES = (
		('Msc','Msc'),
		('PhD','PhD'),
		)

	proposed_degree = models.CharField(max_length = 3, choices = DEGREE_CHOICES)

	other_funding = models.TextField(max_length=200)
	referee_details = models.TextField(max_length =200)
	degree_1 = models.CharField(max_length=200, blank =True, verbose_name=('Degree 1'))
	f_o_study_1 = models.CharField(max_length=200, blank = True,verbose_name=('Field of study 1'))
	major_sub_1 = models.CharField(max_length=200, blank = True,verbose_name=('Major Subject 1'))
	institution_1 = models.CharField(max_length=200, blank = True, verbose_name=('Institution 1'))
	year_obtained_1 = models.CharField(max_length=10, blank =True,verbose_name=('Year obtained 1'))
	degree_2 = models.CharField(max_length=200, blank =True, verbose_name=('Degree 2'))
	f_o_study_2 = models.CharField(max_length=200, blank = True,verbose_name=('Field of study 2'))
	major_sub_2 = models.CharField(max_length=200, blank = True, verbose_name=('Major subject 2'))
	institution_2 = models.CharField(max_length=200, blank = True, verbose_name=('Institution 2'))
	year_obtained_2 = models.CharField(max_length=10, blank = True,verbose_name=('Year obtained 2'))
	degree_3 = models.CharField(max_length=200, blank =True, verbose_name=('Degree 3'))
	f_o_study_3 = models.CharField(max_length=200, blank = True, verbose_name=('Field of study 3'))
	major_sub_3 = models.CharField(max_length=200, blank = True, verbose_name=('Major subject 3'))
	institution_3 = models.CharField(max_length=200, blank = True, verbose_name=('Institution 3'))
	year_obtained_3 = models.CharField(max_length=10, blank=True,verbose_name=('Year obtained 3'))
	degree_4 = models.CharField(max_length=200, blank =True,verbose_name=('Degree 4'))
	f_o_study_4 = models.CharField(max_length=200, blank = True,verbose_name=('Field of study 4'))
	major_sub_4 = models.CharField(max_length=200, blank = True,verbose_name=('Major subject 4'))
	institution_4 = models.CharField(max_length=200, blank = True, verbose_name=('Institution 4'))
	year_obtained_4 = models.CharField(max_length=10, blank= True, verbose_name=('Year obtained 4'))
	"""database will store the directory of the file in the database instead of the file to avoid database
	perfomance issues
	"""
	#personal_statement=models.ContentTypeRestrictedFileField(upload_to='media/uploads/%Y/%m', content_types = ['pdf'], max_upload_size=2621440) # sets default upload file and saves files in the order of dates
	personal_statement=models.FileField(upload_to='applicantfiles', null=True, blank=True)
	cv=models.FileField(upload_to='applicantfiles', null=True, blank=True)
	transcript=models.FileField(upload_to='applicantfiles', null=True, blank=True)
	ref_letter=models.FileField(upload_to='applicantfiles', null=True, blank=True)
	id_copy=models.FileField(upload_to='applicantfiles', null=True, blank=True)
	article=models.FileField(upload_to='applicantfiles', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, )
	#article=models.FileField(upload_to='media/uploads/%Y/%m', default='uploads/uploadtestdocument.pdf')
	#function below returns select table data columns on the admin side
	class Meta:
		verbose_name_plural = "Internal Bursaries"

	def __str__(self):
		return self.first_name + ' | '  + str (self.surname) + ' | '  + str (self.telephone_number)+ ' | '  + str (self.email) + ' | ' + str(self.id) + '|' + str(self.created_at) +'|' + str(self.proposed_degree) + '|'+ str(self.full_part_time)
