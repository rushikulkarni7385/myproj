from django import forms
from django.contrib.auth.models import User
from testapp.models import *

class SignUpform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]

class HydJobsform(forms.ModelForm):
    class Meta:
        model=Hyd_Jobs
        fields='__all__'


class ChennaiJobsform(forms.ModelForm):
    class Meta:
        model=Chennai_Jobs
        fields='__all__'


class PuneJobsform(forms.ModelForm):
    class Meta:
        model=Pune_Jobs
        fields='__all__'

class BangloreJobsform(forms.ModelForm):
    class Meta:
        model=Banglore_Jobs
        fields='__all__'