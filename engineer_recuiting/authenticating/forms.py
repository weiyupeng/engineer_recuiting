from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        cd=self.cleaned_data
        user_name=cd.get('username')

        if len(user_name)<3:
            raise forms.ValidationError("please put more characthers")

        return user_name

class UserCreationForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model=User
        fields=['username','password','confirm_password','email']

    def clean(self):
        cd=self.cleaned_data
        user_name=cd.get('username')
        comfirm_password=cd.get('confirm_password')
        password = cd.get('password')

        if len(user_name)<3:
            raise forms.ValidationError("please put more characthers")

        if '_' in user_name:
            raise forms.ValidationError("you can't contain '_' in your name")

        if comfirm_password != password:
            raise forms.ValidationError("the password doesn't match")

        if len(password)<6:
            raise forms.ValidationError("the passcode is too short")

        return cd

