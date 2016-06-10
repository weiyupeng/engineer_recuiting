from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class DepartmentProfile(models.Model):
    user=models.OneToOneField(User)
    company=models.ForeignKey(User,related_name='departments')
    department_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=15,)
    contacter=models.CharField(max_length=20)
    description=models.TextField(blank=True,null=True)
class CreateDepartmentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    class Meta:
        model=DepartmentProfile
        fields=['department_name','phone','contacter','description','password','confirm_password','email']

STATE=(('BJ','BJ'),('TJ','TJ'))
CITY=(('HD','HD'),('BH','BH'))
BUSSINESS_TYPE=(('CS','computer science'),('EE','electric engnieer'))
AREAR_TYPE=(('CS','computer science'),('EE','electric engnieer'))
APPROVED_STATUS=(('a','approved'),('w','waiting'),('d','denied'),('e','ending'))
class RecruitmentInformation(models.Model):
    title=models.CharField(max_length=100)
    department=models.ForeignKey(User,verbose_name='recruitment_infos',help_text='your department',)
    date=models.DateField()
    begin_date=models.DateField()
    end_date=models.DateField()
    salary=models.PositiveIntegerField()
    major_area=models.CharField(max_length=2,choices=AREAR_TYPE)
    description=models.CharField(max_length=200)
    state=models.CharField(max_length=2,choices=STATE)
    city=models.CharField(max_length=2,choices=CITY)
    status=models.CharField(max_length=2,choices=APPROVED_STATUS,default='w')
    reason_of_deny=models.TextField(max_length=300,blank=True,null=True)
class CreateRecruitmentForm(forms.ModelForm):
    class Meta:
        model=RecruitmentInformation
        exclude=['department','status','reason_of_deny','date','reason_of_deny']
class DeniedReasonForm(forms.ModelForm):
    class Meta:
        model=RecruitmentInformation
        fields=['reason_of_deny']