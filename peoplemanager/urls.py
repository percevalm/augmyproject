
from django.urls import path, include
from django.conf.urls import url, include
from . import views
from .views import StaffDetailDetailView
from archivesuploads.views import ArchivesuploadsListView


urlpatterns = [
   path('corestaff/',views.corestaff, name ='corestaff') ,
   path('postdcrfellows/',views.postdcrfellows, name ='postdcrfellows') ,
   path('researchafellows/',views.researchafellows, name ='researchafellows') ,
   path('students/',views.students, name ='students') ,
   path('steering_committee/',views.steering_committee, name ='steering_committee') ,
   path('scientific_advisory/',views.scientific_advisory, name ='scientific_advisory') ,
   path('staffdetail/<int:pk>/', StaffDetailDetailView.as_view(), name='staffdetail'),
   path('person/',views.ArchivesuploadsListView.as_view(), name ='person'),

   ]
