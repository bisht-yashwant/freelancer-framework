from django.contrib import admin
from .models import Recruitment,Candidate,profile

# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
  list_display = ('fullname',)


admin.site.register(Recruitment)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(profile)
