from django.forms import ModelForm
from django import forms
from .models import Candidate

class input_profile(forms.Form):
  # username
  user_image = forms.ImageField()
  user_name = forms.CharField(max_length=100)
  user_mid_name = forms.CharField(max_length=100)
  user_lst_name = forms.CharField(max_length=100)
  # user id
  user_id = forms.CharField(max_length=120)
  # password
  user_pass = forms.CharField(widget=forms.PasswordInput())
  user_con_pass = forms.CharField(widget=forms.PasswordInput())
  # persional detail
  user_age = forms.CharField(max_length=100)
  user_address = forms.Textarea()
  user_eamil = forms.EmailField()
  user_phone = forms.IntegerField()
  user_education = forms.Textarea()
  # skills
  user_profession = forms.Textarea()
  user_skills = forms.CharField()
  # social site
  website = forms.URLField()
  github = forms.URLField()
  twitter = forms.URLField()
  instagram = forms.URLField()
  facebook = forms.URLField()
      
class CandidateProfile(ModelForm):
#  name = user_name
  class Meta:
    model = Candidate
    exclude = []
