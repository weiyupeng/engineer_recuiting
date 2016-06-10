from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    from_user=models.ForeignKey(User,related_name='my_sending')
    to_user=models.ForeignKey(User,related_name='my_receiver')
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=1000)
    is_read=models.BooleanField(default=False)
class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['content']