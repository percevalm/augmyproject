from django import forms
from .models import Intbursary
from django.contrib import admin
##aded for file size limit
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class IntbursaryForm(forms.ModelForm):
	class Meta:
		model = Intbursary
		fields = '__all__'

	def clean_surname(self):
		surname =self.cleaned_data.get('surname')
		if surname =='':
			raise forms.ValidationError("This field cannot be left empty!")
		return surname

		"""code malfunctioning 2019-02-06
def clean_content(self):
    content = self.cleaned_data['personal_statement']
    content_type = content.content_type.split('/')[0]
    if content_type in settings.CONTENT_TYPES:
        if content._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    else:
        raise forms.ValidationError(_('File type is not supported'))
    return content
"""

	#all fieldsthat we have	["surname","first_name","id_number","nationality","race","gender","telephone_number","email","employed","employed_at","full_part_time","employed_study", "employed_study_details","proposed_degree","other_funding","referee_details","degree_1","f_o_study_1","major_sub_1","institution_1","year_obtained_1","personal_statement"]