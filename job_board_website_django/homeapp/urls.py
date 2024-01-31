from django.contrib import admin
from django.urls import path, include
from .views import (home_view,
    employee_view,
    employer_view,
    employee_login_view,
    employee_signup_view,
    employer_signup_view,
    employer_login_view,
        )

app = "homeapp"
urlpatterns = [ 

    path('', home_view ,name = "home_url"),
    path('employee/', employee_view ,name = "employee_url"),
    path('employer/', employer_view ,name = "employer_url"),
    path('employee/employee_login/', employee_login_view ,name = "employee_login_url"),
    path('employee/employee_signup/', employee_signup_view ,name = "employee_signin_url"),
    path('employer/employer_signup/', employer_signup_view ,name = "employer_signup_url"),
    path('employer/employer_login/', employer_login_view ,name = "employer_login_url"),
    

]