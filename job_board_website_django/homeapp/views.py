from django.template import loader
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render
from employee_app.forms import EmployeeSignUpForm, EmployeeLoginForm
from employee_app.models import Employee_model
from employer_app.forms import EmployerSignupForm, EmployerLoginForm
from employer_app.models import EmployerModel
from django.contrib.auth.decorators import login_required
# Create your views here.



def home_view(request):
    #template = loader.get_template ("test.html")
    return render(request, "Home.html", {})

def employee_view( request,):
    template = loader.get_template ("employee.html")
    return HttpResponse(template.render({}, request))

def employer_view(request,):
    template = loader.get_template ("employer.html")
    return HttpResponse(template.render())

def employee_login_view(request,):
    form = EmployeeLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("Employee_name")
        employeerecord = get_object_or_404(Employee_model, Employee_name = username)
        if (employeerecord.password == form.cleaned_data.get("password") and employeerecord.active):
            return HttpResponsePermanentRedirect(f"/employee_app/{employeerecord.Tel_No}/")
        else:
            return HttpResponse(
                "<center>invalid user<br> try again<br>or try account's registration/activation <br>here<a href = \"../std_signup/\">Sign up</a></center>"
                )

    context = {
        "form" : form
    }
    template = loader.get_template ("employeelogin.html")
    return HttpResponse(template.render(context, request))

def employer_login_view(request,):
    form = EmployerLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("admin_name")
        adminrecord = get_object_or_404(EmployerModel, admin_name = username)
        if (adminrecord.admin_password == form.cleaned_data.get("admin_password") and adminrecord.active):
            return HttpResponsePermanentRedirect(f"/employer_app/{adminrecord.admin_id}/")
        else:
            return HttpResponse(
                "<center>invalid user<br> try again<br>or try account's registration/activation <br>here<a href = \"../employer_signup/\">Sign up</a></center>"
                )
       

    context = {
        "form" : form
    }
    template = loader.get_template ("employerlogin.html")
    return HttpResponse(template.render(context, request))


@login_required
def employee_signup_view(request):
    form = EmployeeSignUpForm()
    if request.method == "POST":
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            b = get_object_or_404(Employee_model, Employee_name = a["Employee_name"] )
            if (a['Tel_No'] == b.Tel_No and a["email"] == b.email and a["Employee_name"] == b.Employee_name):
                if (b.active != True):
                    b.active = True
                else:
                    return HttpResponse("<p><h1>your account is already active</h1><br>try logging in.<p>")
                b.email =a["email"]
                b.password = a["password"]
                b.save()
            else:
                return HttpResponse("<p><h1>There is no record of you in our system.</h1><br>Please check your data entry carefully</p>")
    form = EmployeeSignUpForm()
    context = {
        "form" : form
    }
    template = loader.get_template ("employeeSignUp.html")
    return HttpResponse(template.render(context, request)) 

@login_required
def employer_signup_view(request):
    form = EmployerSignupForm()
    if request.method == "POST":
        form = EmployerSignupForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            b = get_object_or_404(EmployerModel, admin_id = a["employer_no"])
            if(a["admin_name"] == b.admin_name and a["employer_no"]==b.admin_id and b.admin_email == a["admin_email"]):
                if (b.active != True):
                    b.active = True
                else: 
                    return HttpResponse("<p><h1>your account is already active</h1><br>try logging in.<p>")
                b.admin_password = a["admin_password"]
                b.employer_no = a["employer_no"]
                b.save()
            else:
                return HttpResponse("<p><h1>There is no record of you in our system.</h1><br>Please check your data entry carefully</p>")
    form = EmployerSignupForm()
    context = {
        "form" : form
    }
    template = loader.get_template ("employerSignUp.html")
    return HttpResponse(template.render(context, request))  


