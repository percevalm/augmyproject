from django.shortcuts import render

from django.views import generic
from django.views.generic import ListView, View
from .models import News, Event, Opportunity, Newsletters

# Create your views here.
class NewsListView(ListView):
    #model = Archivesuploads
    context_object_name = 'object_list'
    queryset = News.objects.order_by('id')#[:2] add this to limit the number of publications
    template_name = "home.html"


def home(request):

   return render(request, "home.html", {})

   return redirect('home')
