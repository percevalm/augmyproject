
from django.urls import path, include
from .views import NewsListView
from . import views
#from mysite.search import views

urlpatterns = [
   path('',views.NewsListView.as_view(), name ='news'),
]
