from django.db import models


class profile(models.Model):     
      def profilepic(self):
            work_link = models.CharField()
      def skills(self):
            skills = models.CharField()
      def social(self):
            website = models.URLField()
            github = models.URLField()
            twitter = models.URLField()
            instagram = models.URLField()
            facebook = models.URLField()
      user_id = models.CharField(max_length= 120)
      user_name = models.CharField(max_length=100)
      user_age = models.CharField(max_length=100)
      user_eamil = models.EmailField()
      user_phone = models.IntegerField()
      user_profession = models.TextField()  
  
# Table
class Recruitment(models.Model):
  # company name
  company_name = models.CharField(max_length=150)

  # position
  position_name = models.CharField(max_length=100)

  # description
  description = models.TextField(max_length=100)

  # requirement
  requirement = models.TextField()

  # column what to show
  def __str__(self):
    return self.position_name

GENDER_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class Candidate(models.Model):
  pic = models.ImageField(upload_to='profilepic/', null=True, blank=True)
  # name
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50, null=True, blank=True)
  last_name  = models.CharField(max_length=50, null=True, blank=True)

  # personal detail
  recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)
  dob = models.DateField("Date of Birth")
  primary_phone = models.CharField(max_length=12)
  secondary_phone = models.CharField(max_length=12, null=True, blank=True)
  address = models.TextField()
  email = models.EmailField(null=True, blank=True)
  linkedin = models.URLField(null=True, blank=True)
  github = models.URLField(null=True, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

  # education
  bachelor_from = models.CharField(max_length=250,null=True, blank=True)
  masters_from = models.CharField(max_length=250, null=True, blank=True)
  certificates = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)


  # resume
  resume = models.FileField(upload_to='resume/')

  def image_tag(self):
    from django.utils.html import mark_safe
    return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.pic.url))
    image_tag.short_description = 'Image'

  def fullname(self):
    return f"{self.first_name} {self.middle_name} {self.last_name} "
