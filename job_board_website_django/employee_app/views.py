from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from homeapp.models import Jobs    
from homeapp.forms import Search_form
from django.template import loader
import datetime as dt
from employee_app.models import Employee_model

# Create your views here.

def denied_access_report(request,Tel_No):
    return HttpResponse("<h2><font color = \"red\" type =\"Tempus sans ITC\"><center>Sorry, you can't do that.<br>Only employers can post jobs.</center></font></h2>")

def employee_job_search_veiw(request, Tel_No):

    form = Search_form()
    query_set = Jobs.objects.all()
    if request.method == "POST":
        form = Search_form(request.POST)
        if form.is_valid():
            if (request.POST['by'] == "job_title"):
                query_set = Jobs.objects.filter(
                job_title__icontains = request.POST.get('your_search')
                )
            elif(request.POST['by'] == "company"):
                query_set = Jobs.objects.filter(
                company__icontains = request.POST.get('your_search')
                )
            elif(request.POST['by'] =="job_subject_area"):
                query_set = Jobs.objects.filter(
                job_subject_area__icontains = request.POST.get('your_search')
                )
            elif(request.POST['by']=="job_availability"):
                query_set = Jobs.objects.filter(
                job_availability__icontains = request.POST.get('your_search')
                )
            else:
                return HttpResponse("<h2><font color = \"red\" type =\"Tempus sans ITC\"><center>No jobs found.</center></font></h2>")
            # query_set = Books.objects.filter(
            #     request.POST['by']__icontains = request.POST.get('keystrings')
            #     )
    context = {
        'form'       :  form,
        'query_set'  :  query_set,
        "user"       :  Tel_No,
        "app"    :  "employee_app",
    }
    return HttpResponse(render(request, "search.html" ,context))












