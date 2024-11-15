# apps/accounts/forms.py
from django import forms

class UserProfileForm(forms.Form):
    # Example fields
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
