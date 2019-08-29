from import_export import resources
from myapp.models import Intbursary

class IntbursaryResource(resources.ModelResource):
	class Meta:
		model = Intbursary


