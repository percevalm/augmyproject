from django.db import models

# Create your models here.
class Account(models.Model): # this models allows user to capture a more dynamic way of usernames and passwords
	account_name = models.CharField(max_length=200, null=True, blank=True)
	username = models.CharField(max_length=200, null=True, blank=True)
	password = models.CharField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural = " Accounts, Usernames & Passwords for Sacema "

	def __str__(self):
			return self.account_name + ' | '  + str (self.username) + '|' + str (self.password) + '|' + str (self.created_at) + '|' + str (self.updated_at)