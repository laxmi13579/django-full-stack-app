from django import forms 
from django.core.validators import validate_email
import re

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# validate with all field, below code use name field validation
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        password_value = cleaned_data.get('password')

        if name_value and len(name_value) < 4:
            self.add_error('name','Enter name greater than 4 character')

        if password_value and len(password_value) < 4:
            self.add_error('password','Enter password greater than 4 character')

        return cleaned_data

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
