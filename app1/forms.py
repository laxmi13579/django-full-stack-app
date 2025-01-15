from django import forms 
from django.core.validators import MaxLengthValidator, MinLengthValidator
import re

from app1.models import Profile

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_name', 'email', 'password']


# custom validator to check the length of password
# built in validator to check the length of name
def password_validator(value):
    if len(value) < 4:
        raise forms.ValidationError('Password should be greater than 4 digit')
class RegisterForm(forms.Form):
    student_name = forms.CharField(validators=[MinLengthValidator(5), MaxLengthValidator(100)], error_messages={'required': 'Name is required'})
    teacher_name = forms.CharField(validators=[MinLengthValidator(5), MaxLengthValidator(100)], error_messages={'required': 'Name is required'})
    email = forms.CharField(max_length=100, error_messages={'required': 'Email is required'})
    password = forms.CharField(widget=forms.PasswordInput, validators=[password_validator], error_messages={'required': 'Password is required'})


# validate with all field, below code use name field validation
    # def clean(self):
    #     cleaned_data = super().clean()
    #     name_value = cleaned_data.get('name')
    #     password_value = cleaned_data.get('password')

    #     if name_value and len(name_value) < 4:
    #         self.add_error('name','Enter name greater than 4 character')

    #     if password_value and len(password_value) < 4:
    #         self.add_error('password','Enter password greater than 4 character')

    #     return cleaned_data

# validate with specific field, below code use name field validation
# class RegisterForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean_name(self):
#         name_value = self.cleaned_data['name']

#         if len(name_value) < 4:
#             raise forms.ValidationError('Enter name greater than 4 character')
#         return name_value
