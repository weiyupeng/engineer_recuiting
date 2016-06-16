from django.db import transaction
from django.shortcuts import render
from django.utils.html import escape
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from engineer_recuiting import settings
from engineer_recuiting.authenticating.forms import LoginForm,UserCreationForm
from engineer_recuiting.company.models import CompanyProfile,CompanyProfileForm
from engineer_recuiting.engineer.forms import EngineerProfile,EngineerCreationForm

"""
this viev is concern about amdining anything related with login, sign out, sending confirm email and stuff like that
"""


def create_user(req,type):

    '''create user , ang baesd on the differnt type of user,we create the different profile for them '''

    if req.method=='POST':
        #create user
        if type=='user':
            form=UserCreationForm(req.POST)
            if form.is_valid():
                return create_user_file(req,form)
            else:
                return render(req,'createuser.html',{'form':form})

        #create engineer
        if type=='engineer':
            form=EngineerCreationForm(req.POST)
            if form.is_valid():
                return create_engineer_file(req,form)
            else:
                return render(req,'createuser.html',{'form':form})
        if type=='company':
            form=CompanyProfileForm(req.POST,req.FILES)
            if form.is_valid():
                return create_company_file(req,form)
            else:
                return render(req,'createuser.html',{'form':form})
    else:
        #create user
        if type=='user':
            form=UserCreationForm()

        #create engnieer
        if type=='engineer':
            form=EngineerCreationForm()
        if type=='company':
            form=CompanyProfileForm()

        return render(req,'createuser.html',{'form':form})

#called by create_user()
def create_user_file(req,form):
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

#called by create_user()
def create_engineer_file(req,form):
    user=req.user
    if hasattr(user,'engineerprofile') or hasattr(user,'companyprofile') or hasattr(user,'departmentprofile'):
        return HttpResponseRedirect('/hacker')
    else:
        engineer=form.save(commit=False)
        engineer.user=user
        with transaction.atomic():
            engineer.save()
            CONFIRM_URL='http://127.0.0.1:8000/engineer/email_confirm_email={0},id={1}'
            confirm_url=CONFIRM_URL.format(
                #escape is usesd for ignore '/', actually we don;t need it in here but well...
                escape(user.email),
                escape(user.id)
            )
            send_email('email comfirm from our company',confirm_url,user.email)
            return HttpResponseRedirect('/engineer')

#called by create_user
def create_company_file(req,form):
    user=req.user
    if hasattr(user,'engineerprofile') or hasattr(user,'companyprofile') or hasattr(user,'departmentprofile'):
        return HttpResponseRedirect('/hacker')
    else:
        company=form.save(commit=False)
        company.user=user
        company.save()
        return HttpResponseRedirect('/company')


#the fuction to help send email to different user
def send_email(title,content,*to_suer):
    send_mail(title, content, settings.EMAIL_HOST_USER,to_suer ,fail_silently=False)

def log_in(req):
    if req.method=='POST':
        form=LoginForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                return render(req,'login.html',{'form':form,'wrong_password':True})
            user = authenticate(username=username, password=password)
            login(req,user)
            if hasattr(user,'engineerprofile'):
                return HttpResponseRedirect('/engineer/')
            if hasattr(user,'companyprofile'):
                return HttpResponseRedirect('/company')
            if hasattr(user,'departmentprofile'):
                return HttpResponseRedirect('/department/')
            else:
                # haven't create any actor yet...
                return render(req,'createuser.html')

        else:
            return render(req,'login.html',{'form':form})
    else:
        form=LoginForm()
        return render(req,'login.html',{'form':form})

def all_logout(req):
    logout(req)
    return HttpResponseRedirect('/')