from django.contrib.auth.models import Archivesuploads
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['title', 'name', ]