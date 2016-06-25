from django.db import models
from django import forms

from engineer_recuiting.company.models import CompanyProfile
from engineer_recuiting.application.models import Application
from engineer_recuiting.department.views import RecruitmentInformation
# Create your models here.
class ComplainReport(models.Model):

    report_date = models.DateField()
    description = models.TextField()
    complain = models.ForeignKey(Application)



class CompanySearchForm(forms.Form):
    name=forms.CharField(max_length=20)

class CompanyAddMoneyForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['account']
class ChangeApplicationMoneyForm(forms.ModelForm):
    class Meta:
        model = RecruitmentInformation
        fields = ['salary']