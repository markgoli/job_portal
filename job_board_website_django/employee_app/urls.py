from django import urls
from django.urls import path
from . views import employee_job_search_veiw, denied_access_report
app_name = "employee_app"
urlpatterns = [
    path("<int:Tel_No>/",employee_job_search_veiw ,name = "employee search"),
    path("<int:Tel_No>/add_job/",denied_access_report,name = "denied access"),
    ]