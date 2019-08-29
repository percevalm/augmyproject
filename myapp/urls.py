
from django.urls import path, include
from . import views


urlpatterns = [
   path('hello/',views.hello, name ='hello'),
   path('intbursary/',views.intbursary, name ='intbursary'),
   path('',views.home, name ='home') ,
   path('saved/',views.saved, name ='saved') ,
   path('about/',views.about, name ='about') ,
   #path('grappelli/', include('grappelli.urls')),
] 
