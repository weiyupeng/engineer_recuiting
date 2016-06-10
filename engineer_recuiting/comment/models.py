from django.db import models
from django import forms
from django.contrib.auth.models import User
from engineer_recuiting.application.models import Application
# Create your models here.

class Comment(models.Model):
    application=models.OneToOneField(Application)
    engineer_starts=models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),default=3)
    department_starts=models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),default=3)
    engineer_review=models.CharField(null=True,max_length='300',blank=True)
    department_review=models.CharField(null=True,max_length='300',blank=True)

class EngieerComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['engineer_starts','engineer_review']

class DepartmentComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['department_starts','department_review']