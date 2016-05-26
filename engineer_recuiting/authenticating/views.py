from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import transaction
# Create your views here.

from engineer_recuiting.engineer.forms import EngineerProfile,EngineerCreationForm,UserCreationForm
def create_user(req,type):
    if req.method=='POST':
        if type=='user':
            form=UserCreationForm(req.POST)
            if form.is_valid():
                # js will handle the problem of passcode is not match ,passcode/account is not valid
                try:
                    User.objects.get(username=form.cleaned_data.get('username'))
                    return render(req,'createuser.html',{'form':form,'name_used':True})
                except:
                    with transaction.atomic():
                        username = form.cleaned_data.get('username')
                        email = form.cleaned_data.get('email')
                        password = form.cleaned_data.get('password')
                        User.objects.create_user(username=username,password=password,email=email)
                        user = authenticate(username=username, password=password)
                        login(req,user)
                        return render(req,'createuser.html')
            else:
                return render(req,'createuser.html',{'form':form})
        if type=='engineer':
            form=EngineerCreationForm(req.POST)
            user=req.user
            if hasattr(user,'engineerprofile') or hasattr(user,'companyprofile') or hasattr(user,'departmentprofile'):
                return HttpResponseRedirect('/hacker')
            else:
                engineer=form.save(commit=False)
                engineer.user=user
                engineer.save()
                return HttpResponseRedirect('engineer_homepage.html')

    else:
        #create user
        if type=='user':
            form=UserCreationForm()
        #create engnieer
        if type=='engineer':
            form=EngineerCreationForm()
        return render(req,'createuser.html',{'form':form})
