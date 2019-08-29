from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import StaffDetail, PeopleDetail, StudentDetail



from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone # to display date and time as per timezone
from django.views.generic import ListView, DetailView, View, TemplateView
from archivesuploads.models import Archivesuploads, Archivetypes, Interests

# Create your views here.
#this code wil display the publications on the publications page profile
class StaffDetailDetailView(DetailView):
    model = StaffDetail
    template_name = 'person.html'

#this code wil display the publications on persons profile
#class ArchivesuploadsList(ListView):
    #model = Archivesuploads
    #context_object_name = 'object_list'
    #queryset = Archivesuploads.objects.order_by('-publication_date')   #[:2] add this to limit the number of publications
    #template_name = "person.html"




class ArchivesuploadsListView(ListView):
    #model = Archivesuploads
    context_object_name = 'object_list'
    queryset = Archivesuploads.objects.all()#[:2] add this to limit the number of publications
    template_name = "person.html"


# Create your views here.
def corestaff(request):
    #peopledetails = PeopleDetail.objects.filter(id=4).select_related() #shows on person online
    staffdetails = StaffDetail.objects.order_by('id').filter(category__icontains='CS').filter(is_active__iexact='true')#code will list all records without joins

    # Assumes you have a row with a primary key of 1
    #staffdetail = StaffDetail.objects.get(pk=1)

# get the email of the reporter for the article
    #peopledetails = staffdetail.PeopleDetail.firstnames


    return render(request, "corestaff.html", {'staffdetails': staffdetails})


#def person(request):

    #return render(request, "person.html", {})


def postdcrfellows(request):
    staffdetails = StaffDetail.objects.filter(category__iexact='PDRF').filter(is_active__iexact='true')# this selection is hard wired on the model category options as in the table!

    return render(request, "postdcrfellows.html", {'staffdetails': staffdetails})


def researchafellows(request):
    staffdetails = StaffDetail.objects.filter(category__iexact='RAF').filter(is_active__iexact='true')# this selection is hard wired on the model category options as in the table!
    return render(request, "researchafellows.html", {'staffdetails': staffdetails})

def scientific_advisory(request):
    staffdetails = StaffDetail.objects.filter(category__icontains='SUSAC').filter(is_active__iexact='true')# this selection is hard wired on the model category options as in the table!
    return render(request, "scientific_advisory.html", {'staffdetails': staffdetails})

def steering_committee(request):
    staffdetails = StaffDetail.objects.filter(category__icontains='SC' ).filter(is_active__iexact='true')# this selection is hard wired on the model category options as in the table!
    return render(request, "steering_committee.html", {'staffdetails': staffdetails})

def students(request):
    phdstudentdetails = StudentDetail.objects.filter(degree__iexact='PhD').filter(currently_registered__iexact='Yes')
    mscstudentdetails = StudentDetail.objects.filter(degree__iexact='MSc').filter(currently_registered__iexact='Yes')
    erfstudentdetails = StudentDetail.objects.filter(degree__iexact='ERF').filter(currently_registered__iexact='Yes')
    honsstudentdetails = StudentDetail.objects.filter(degree__iexact='Hons').filter(currently_registered__iexact='Yes')

    context = {
        'phdstudentdetails': phdstudentdetails,
        'mscstudentdetails': mscstudentdetails,
        'erfstudentdetails': erfstudentdetails,
        'honsstudentdetails': honsstudentdetails
    }
    return render(request, "students.html", context)



def home(request):
   return render(request, "home.html", {})
   return redirect('home')
