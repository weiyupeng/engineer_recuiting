from django import forms
from engineer_recuiting.engineer.models import EngineerProfile,CertificationOfDegree,SkillCertification,User


class EngineerCreationForm(forms.ModelForm):
    class Meta:
        model=EngineerProfile
        exclude=['review_score','status','user']
class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    class Meta:
        model=User
        fields=['username','password','confirm_password','email']