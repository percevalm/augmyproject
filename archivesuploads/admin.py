from django.contrib import admin
from .models import Archivesuploads, Archivetypes, Interests
from django.utils.safestring import mark_safe
# Register your models here.


class ArchivesuploadsAdmin(admin.ModelAdmin):
	list_display = ('id','journal','archivetype','name','title','url','publication_date','created','general_doi','file')
	list_filter = ['publication_date','created']
	ordering =	['publication_date']


admin.site.register(Archivesuploads, ArchivesuploadsAdmin)

class ArchivetypesAdmin(admin.ModelAdmin):
	list_display = ('id','name','description')
	ordering = ['id']
admin.site.register(Archivetypes, ArchivetypesAdmin)

class InterestsAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','created')
	ordering = ['id']
admin.site.register(Interests, InterestsAdmin)