from django.shortcuts import render, redirect
from .models import Intbursary
from .forms import IntbursaryForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone # to display ate and time as per timezone

# Create your views here.
#line 12 to line 37 is an if statement to post all entries from the front end interface into the intbursary table
#All table columns are listed as they are as
def intbursary(request):
	if  request.method == 'POST':
		if request.POST['surname'] and request.POST['first_name'] and request.POST['id_number'] and request.POST['nationality'] and request.POST['race'] and request.POST['gender'] and request.POST['telephone_number'] and request.POST['email'] and request.POST['employed'] and request.POST['employed_at'] and request.POST['full_part_time'] and request.POST['employed_study'] and request.POST['employed_study_details'] and request.POST['proposed_degree'] and request.POST['other_funding'] and request.POST['referee_details'] and request.POST['degree_1'] or "-"  and request.POST['f_o_study_1'] or "-" and request.POST['major_sub_1'] or "-" and request.POST['institution_1'] or "-" and request.POST['year_obtained_1'] or " " and request.FILES['personal_statement'] and request.FILES['cv'] and request.FILES['transcript'] and request.FILES['ref_letter'] and request.FILES['id_copy'] and request.FILES['article'] and request.POST['degree_2'] or "-" and request.POST['f_o_study_2'] or "-" and request.POST['major_sub_2'] or "-" and request.POST['institution_2'] or "-" and request.POST['year_obtained_2'] or " " and request.POST['degree_3'] or "-" and request.POST['f_o_study_3'] or "-" and request.POST['major_sub_3'] or "-" and request.POST['institution_3'] or "-" and request.POST['year_obtained_3'] or " " and request.POST['degree_4'] or "-" and request.POST['f_o_study_4'] or "-" and request.POST['major_sub_4'] or "-" and request.POST['institution_4'] or "-" and request.POST['year_obtained_4'] or " " :
			form = Intbursary
			intbursaryapps = Intbursary()
			intbursaryapps.surname = request.POST['surname']
			intbursaryapps.first_name = request.POST['first_name']
			intbursaryapps.id_number = request.POST['id_number']
			intbursaryapps.nationality = request.POST['nationality']
			intbursaryapps.race = request.POST['race']
			intbursaryapps.gender = request.POST['gender']
			intbursaryapps.telephone_number = request.POST['telephone_number']
			intbursaryapps.email = request.POST['email']
			intbursaryapps.employed = request.POST['employed']
			intbursaryapps.employed_at = request.POST['employed_at']
			intbursaryapps.full_part_time = request.POST['full_part_time']
			intbursaryapps.employed_study = request.POST['employed_study']
			intbursaryapps.employed_study_details = request.POST['employed_study_details']
			intbursaryapps.proposed_degree = request.POST['proposed_degree']
			intbursaryapps.other_funding = request.POST['other_funding']
			intbursaryapps.referee_details = request.POST['referee_details']
			intbursaryapps.degree_1 = request.POST['degree_1'] or "-" # " " will allow posting of an empty form
			intbursaryapps.f_o_study_1 = request.POST['f_o_study_1'] or "-" # " " will allow posting of an empty form
			intbursaryapps.major_sub_1 = request.POST['major_sub_1'] or "-" # " " will allow posting of an empty form
			intbursaryapps.institution_1 = request.POST['institution_1'] or "-" # " " will allow posting of an empty form
			intbursaryapps.year_obtained_1 = request.POST['year_obtained_1'] or "0000-00-00" # " " will allow posting of an empty form
			intbursaryapps.degree_2 = request.POST['degree_2'] or "-" # " " will allow posting of an empty form
			intbursaryapps.f_o_study_2 = request.POST['f_o_study_2'] or "-" # " " will allow posting of an empty form
			intbursaryapps.major_sub_2 = request.POST['major_sub_2'] or "-" # " " will allow posting of an empty form
			intbursaryapps.institution_2 = request.POST['institution_2'] or "-" # " " will allow posting of an empty form
			intbursaryapps.year_obtained_2 = request.POST['year_obtained_2'] or "0000-00-00" # " " will allow posting of an empty form
			intbursaryapps.degree_3 = request.POST['degree_3'] or "-" # " " will allow posting of an empty form
			intbursaryapps.f_o_study_3 = request.POST['f_o_study_3'] or "-" # " " will allow posting of an empty form
			intbursaryapps.major_sub_3 = request.POST['major_sub_3'] or "-" # " " will allow posting of an empty form
			intbursaryapps.institution_3 = request.POST['institution_3'] or "-" # " " will allow posting of an empty form
			intbursaryapps.year_obtained_3 = request.POST['year_obtained_3'] or "0000-00-00" # " " will allow posting of an empty form
			intbursaryapps.degree_4 = request.POST['degree_4'] or "-" # " " will allow posting of an empty form
			intbursaryapps.f_o_study_4 = request.POST['f_o_study_4'] or "-" # " " will allow posting of an empty form
			intbursaryapps.major_sub_4 = request.POST['major_sub_4'] or "-" # " " will allow posting of an empty form
			intbursaryapps.institution_4 = request.POST['institution_4'] or "-" # " " will allow posting of an empty form
			intbursaryapps.year_obtained_4 = request.POST['year_obtained_4'] or "0000-00-00" # " " will allow posting of an empty form
			intbursaryapps.personal_statement = request.FILES['personal_statement']
			intbursaryapps.cv = request.FILES['cv']
			intbursaryapps.transcript = request.FILES['transcript']
			intbursaryapps.ref_letter = request.FILES['ref_letter']
			intbursaryapps.id_copy = request.FILES['id_copy']
			intbursaryapps.article = request.FILES['article']
			intbursaryapps.created_at = timezone.datetime.now()

			intbursaryapps.save()
			messages.success(request,('Your Internal Bursary Application has been Received. The postgraduate committee will revert to you with feedback'))
			return render(request,'intbursary.html',{})
	else:
		   return render(request, 'intbursary.html', {})

def hello(request):
  return render(request, "hello.html", {})

def about(request):
   return render(request, "about.html", {})

def home(request):
   return render(request, "home.html", {})

def saved(request):
   return render(request, "saved.html", {})
   return redirect('home')
