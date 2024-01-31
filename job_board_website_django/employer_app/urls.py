from django import urls
from django.urls import path
from . views import add_job_veiw, find_job_view

app_name = "employer_app"
urlpatterns = [
    path("<int:admin_id>/",find_job_view, name = "find book url"),
    path("<int:admin_id>/add_job/",add_job_veiw, name = "denied"),
    
   ]