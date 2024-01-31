from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from homeapp.models import Jobs
from homeapp.forms import Search_form , Bookform
from django.template import loader
import datetime as dt
import json


# Create your views here.

# def borrow_book_view( request, std_number, bk_id ):
#         return HttpResponse(
#             "<h2><font color = \"red\" type =\"Tempus sans ITC\"><center>Denied access<br>employer cant borrow books</center></font></h2>"
#             )
        

def find_job_view( request, admin_id ):
    query_set = Jobs.objects.all()
    form  = Search_form()
    if request.method == "POST":
        form  = Search_form( request.POST )
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
            
    context = {
        'form'    : form,
        'query_set' : query_set,
        "user": admin_id,
        "app" : "employer_app"
    }
    return HttpResponse( render( request, "searchEmployer.html" , context ))

        
def add_job_veiw (request, admin_id):
    form = Bookform()
    if request.method == "POST":
        form = Bookform( request.POST)
        if form.is_valid():
            form.save()
            form = Bookform()

    template = loader.get_template("add_job.html")
    context = {
        "form" : form
    }
    return HttpResponse(template.render(context, request))

