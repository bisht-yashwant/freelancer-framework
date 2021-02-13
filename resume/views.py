from django.shortcuts import render, HttpResponse
from .forms import CandidateProfile, input_profile
from django.views import View

def profile_forms(request):
  if request.method == "POST":
    form = input_profile(request.POST)
    if form.is_valid():
      image = form.cleaned_data['user_image']
      name = form.cleaned_data['user_name']
      mid_name = form.cleaned_data['user_mid_name']
      lst_name = form.cleaned_data['user_lst_name']
      id = form.cleaned_data['user_id']
      password = form.cleaned_data['user_pass']
      con_passwword = form.cleaned_data['user_con_pass']
      age = form.cleaned_data['user_age']
      address = form.cleaned_data['user_address']
      eamil = form.cleaned_data['user_eamil']
      phone = form.cleaned_data['user_phone']
      education = form.cleaned_data['user_image']
      profession = form.cleaned_data['user_profession']
      skills = form.cleaned_data['user_skills']
      website = form.cleaned_data['website']
      github = form.cleaned_data['github']
      twitter = form.cleaned_data['twitter']
      instagram = form.cleaned_data['instagram']
      facebook  = form.cleaned_data['facebook']
      form.save()
    else:
      form = input_profile()
  return render(request, "home.html", {'form': form})

# Create your views here.
class RecruitmentIndex(View):

  # GET
  def get(self, request):
    return render(request, 'index.html', {"form": CandidateProfile })

  # post
  def post(self, request):

    # generate object from input
    p = CandidateProfile(request.POST)

    # validate
    if p.is_valid():
      # save it
      p.save()
    return self.get(request)
