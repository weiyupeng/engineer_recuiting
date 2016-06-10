from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
from engineer_recuiting.department.models import RecruitmentInformation
BUSSINESS_TYPE=(('CS','computer science'),('EE','electric engnieer'))
AREAR_TYPE=(('CS','computer science'),('EE','electric engnieer'))
DGREE_TYPES=(
    ('H','Highschool'),
    ('B','Banchler'),
    ('M','Master'),
    ('P','PHD'),
)
STATUS_TYPE=(
    ('W','waiting for approve'),
    ('N','normal user'),
    ('B','baned')
)
class CompanyProfile(models.Model):
    user=models.OneToOneField(User)
    company_name=models.CharField(max_length=50)
    bussiness_area=models.CharField(max_length=3,choices=BUSSINESS_TYPE)
    permit_id=models.CharField(max_length=30)
    website=models.URLField(blank=True,null=True)
    phone=models.CharField(max_length=15,)
    contacter=models.CharField(max_length=20)
    permit_img=models.FileField(upload_to='permitImg')
    bank_name=models.CharField(max_length=90)
    account=models.IntegerField(default=10000)
    account_bank_name=models.CharField(max_length=200)
    bank_permit_img=models.FileField(upload_to='BankImg')
    company_telphone=models.CharField(max_length=16)
    credit=models.IntegerField(default=-1)
    status=models.CharField(max_length=3,choices=STATUS_TYPE,default='W')
    description=models.TextField(blank=True,null=True)
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model=CompanyProfile
        exclude=['user','account','credit','status']
class DenyRecruitmentForm(forms.ModelForm):
    class Meta:
        model=RecruitmentInformation
        fields=['reason_of_deny']