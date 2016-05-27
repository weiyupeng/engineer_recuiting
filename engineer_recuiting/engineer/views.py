from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import DetailView,ListView
from django.db import transaction

from engineer_recuiting.engineer.models import User,CertificationOfDegree,EngineerProfile
from engineer_recuiting.engineer.forms import DegreeForm,EngineerCreationForm,ChangePasscodeForm
# # Create your views here.
# def comfirm_required(func):
#     def wrapper(req):
#         if req.user.engineerprofile.status != 'N':
#             return HttpResponseRedirect('/please email confirm first')
#         return func(req)
#     return wrapper

def comfirm_required(func):
    def wrapper(*args, **kw):
        if args[0].user.engineerprofile.status != 'N':
            return HttpResponseRedirect('/please email confirm first')
        return func(*args, **kw)
    return wrapper
@login_required
@ comfirm_required
def show(req):
    # in this page ,we need show application,searching Form,
    user=req.user
    return render(req,'engineer_homepage.html',);
def conform_email(req,email,id):
    try:
        user=User.objects.get(id=int(id))
        if user.email == email:
            print user.email
            user.engineerprofile.status='N'
            user.engineerprofile.save()
            return HttpResponseRedirect('success conform')
        else:
            return HttpResponseRedirect('hacker_email')
    except:
        return HttpResponseRedirect('hacker_email')
@login_required
@ comfirm_required
def manage_info(req,type):
    user=req.user
    if req.method=='POST':
        if type == '':
            # instance argument will help you match the instance and form together
            form=EngineerCreationForm(req.POST,instance=user.engineerprofile)
            if not form.is_valid():
                return render(req,'engineer_info_mange.html',{'form':form})
            form.save()
            return render(req,'engineer_info_mange.html',{'form':form,'is_change':True})
        if type == 'passcode':
            form=ChangePasscodeForm(req.POST)
            if not form.is_valid():
                return render(req,'engineer_info_mange.html',{'form':form})
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return render(req,'engineer_info_mange.html',{'form':form,'is_change':True})
    else:
        if type == '':
            degrees=CertificationOfDegree.objects.filter(owner=user)
            form=EngineerCreationForm(instance=user.engineerprofile)
        if type == 'passcode':
            form = ChangePasscodeForm()
            degrees=None
        return render(req,'engineer_info_mange.html',{'form':form,'degrees':degrees})
@login_required
@comfirm_required
def add_degree(req):
    if req.method=='POST':
        form=DegreeForm(req.POST,req.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.owner=req.user
            instance.save()
            return HttpResponseRedirect('/engineer/my_info_')
        else:
            return render(req,'add_degree.html',{'form':form})
    else:
        form=DegreeForm()
        return render(req,'add_degree.html',{'form':form})
@login_required
@comfirm_required
def delete_degree(req,id):
    try:
        degree=CertificationOfDegree.objects.get(id=int(id))
        if degree.owner!= req.user:
            return HttpResponseRedirect('/hacker change id')
        degree.delete()
        return HttpResponseRedirect('/engineer/my_info_')
    except:
        return HttpResponseRedirect('/hacker change id')

class EngineerprofileView(ListView):
    #it's worong but not finish yet
    model = User
    context_object_name = 'engineer'
    template_name = 'engineer_bussiness_card.html'
    def queryset(self):
        id=int(self.args[0])
        return User.objects.filter(id=id)




