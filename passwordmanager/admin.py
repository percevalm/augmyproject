from django.contrib import admin
from .models import Account
from import_export.admin import ImportExportModelAdmin
from passwordmanager.resources import AccountResource
# Register your models here.(admin.ModelAdmin):
class AccountAdmin(ImportExportModelAdmin):
	list_display = ('id','account_name','username','password','created_at','updated_at')
	ordering =	['id']
	search_fields =('account_name','username')
	list_filter = ['account_name']

admin.site.register(Account, AccountAdmin)
