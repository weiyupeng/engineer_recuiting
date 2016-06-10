from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView,ListView
from django.db import transaction

from engineer_recuiting.engineer.models import User,CertificationOfDegree,EngineerProfile
from engineer_recuiting.engineer.forms import DegreeForm,EngineerCreationForm,ChangePasscodeForm,SearchForm
from engineer_recuiting.department.models import RecruitmentInformation
from engineer_recuiting.application.models import Application
from engineer_recuiting.application.views import applicationStatusChange
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
    if not hasattr(user,'engineerprofile'):
        return HttpResponseRedirect('/hacker not engineer')
    context={}
    context['form']=SearchForm()
    applications=Application.objects.filter(applier=user)
    context['applying_application']=applications.filter(status='w')
    context['waiting_approveing_application']=applications.filter(status='a')
    context['processing_application']=applications.filter(status='s')

    return render(req,'engineer_homepage.html',context)

class SearchingResulteView(ListView):
    template_name = 'searched_recruitment_list.html'
    model = RecruitmentInformation
    paginate_by = 3
    context_object_name = 'recruitments'
    def get_queryset(self):
        form=SearchForm(self.request.GET)
        if form.is_valid():
            beg_data=form.cleaned_data.get('beg_data')
            end_data=form.cleaned_data.get('end_data')
            state=form.cleaned_data.get('state')
            major=form.cleaned_data.get('major')
            object_list=self.model.objects.filter(begin_date__gt=beg_data,end_date__lt=end_data,
                                                             state=state,major_area=major,status='a')
            return object_list
        else:#is it works? no but i will validate by js~~
           #return render(self.request,'engineer_homepage.html',{'form':form,})
            return self.render_to_response('engineer_homepage.html',{'form':form,},self.get_context_data(self))




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
@login_required
#@ operation_required
def changeApplicationStatus(req,app_id,way):
    application=Application.objects.get(id=int(app_id))
    if way=='confirm_application':
        if application.status!='a':
            return HttpResponseRedirect("/you can't do this action" )
        application.recruitment.status='e'
        applicationStatusChange(application,'s')
    if way=='deny_application':
        if application.status!='a':
            return HttpResponseRedirect("/you can't do this action" )
        application.recruitment.status='w'
        applicationStatusChange(application,'s')
    if way=='compaline':
        if application.status!='s':
            return HttpResponseRedirect("/you can't do this action" )
        applicationStatusChange(application,'c')
    application.save()
    return HttpResponseRedirect('/success~~~')



