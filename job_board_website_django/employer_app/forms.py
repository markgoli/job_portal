from logging import PlaceHolder
from django.forms import CharField, ModelForm, PasswordInput
from .models import EmployerModel

class EmployerSignupForm(ModelForm):
    class Meta:
        model = EmployerModel
        fields = [ 'employer_no','admin_name','admin_email','admin_password']

class EmployerLoginForm(ModelForm):
    admin_password = CharField(widget=PasswordInput(
            attrs={
                "placeholder" : "Your password"
            }
            )
        )
    class Meta:
        model = EmployerModel
        fields = ['admin_name','admin_password']