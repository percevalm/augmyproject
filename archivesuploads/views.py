from django.shortcuts import render

from django.views import generic
from django.views.generic import ListView, View
from .models import Archivesuploads, Archivetypes, Interests



# Create your views here.
class ArchivesuploadsListView(ListView):
    #model = Archivesuploads
    context_object_name = 'object_list'
    queryset = Archivesuploads.objects.order_by('-publication_date')#[:2] add this to limit the number of publications
    template_name = "publications.html"


def home(request):

   return render(request, "home.html", {})

   return redirect('home')


