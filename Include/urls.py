
from django.urls import path, include
from .views import ArchivesuploadsListView
from . import views
#from mysite.search import views


urlpatterns = [
   path('publications/',views.ArchivesuploadsListView.as_view(), name ='publications'),
 

]
