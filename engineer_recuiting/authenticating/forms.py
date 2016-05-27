from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password']

class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    class Meta:
        model=User
        fields=['username','password','confirm_password','email']