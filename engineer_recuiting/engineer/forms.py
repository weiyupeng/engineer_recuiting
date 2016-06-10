from django import forms
from engineer_recuiting.engineer.models import EngineerProfile,CertificationOfDegree
STATE=(('BJ','BJ'),('TJ','TJ'))
AREAR_TYPE=(('CS','computer science'),('EE','electric engnieer'))
class EngineerCreationForm(forms.ModelForm):
    class Meta:
        model=EngineerProfile
        exclude=['review_score','status','user']
class DegreeForm(forms.ModelForm):
    class Meta:
        model=CertificationOfDegree
        exclude=['status','owner']
class ChangePasscodeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True,
                                       help_text='js need to help verify if passcode and confirm passcode are the same ' )
class SearchForm(forms.Form):
    beg_data=forms.DateField()
    end_data=forms.DateField()
    state=forms.ChoiceField(choices=STATE)
    major=forms.ChoiceField(choices=AREAR_TYPE)

