from django.forms import CharField, ModelForm, PasswordInput
from .models import Employee_model

class EmployeeSignUpForm(ModelForm):
    class Meta:
        model = Employee_model
        fields = ['Employee_name','Tel_No','email','password']

class EmployeeLoginForm(ModelForm):
    password = CharField(
        widget = PasswordInput(
            attrs={
                "placeholder":"your password"
            }
        )
    )
    class Meta:
        model = Employee_model
        fields = ['Employee_name','password']