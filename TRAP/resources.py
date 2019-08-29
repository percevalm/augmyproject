from import_export import resources

from TRAP.models import Tsetse


class TsetseResource(resources.ModelResource):
	class Meta:
		model = Tsetse
