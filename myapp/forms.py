from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Complaint
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields={'title','description','image'}
        #here using UserCreationForm to access the built in username,password1,password2
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
    #here using clean_data we can give validation conditions
    def clean_email(self):
        email = self.cleaned_data.get('email')#get the email data from submitted form dictionary called clean_data
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email