from django.db import models
from django import forms
from django.contrib.auth.models import User
from engineer_recuiting.department.models import RecruitmentInformation
# Create your models here.
STATUS=(('a','approving'),('w','waiting'),('s','start'),('d','denied'),('f','finishing'),('c','complaining'))
class Application(models.Model):
    date=models.DateField()
    recruitment=models.ForeignKey(RecruitmentInformation)
    applier=models.ForeignKey(User)
    status=models.CharField(max_length=3,choices=STATUS,default='w') # W: means waiting be a validate application,a means it's approving~
    applier_message=models.TextField()
    is_engineer_review=models.BooleanField(default=False)
    is_department_review=models.BooleanField(default=False)
class ApplicationCreateForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=['applier_message']