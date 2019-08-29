from django.shortcuts import render
from .models import Generalenquiries, Physicaladdress, Postaladdress, Place

# Create your views here.
def contactus(request):
    generalenquiries = Generalenquiries.objects.order_by('id')
    physicaladdress = Physicaladdress.objects.order_by('id')
    postaladdress = Postaladdress.objects.order_by('id')
    place = Place.objects.order_by('id')
    return render(request, "contactus.html", {'generalenquiries': generalenquiries,'physicaladdress': physicaladdress, 'postaladdress': postaladdress, 'place': place})


def home(request):
	    
   return render(request, "home.html", {})

   return redirect('home')
