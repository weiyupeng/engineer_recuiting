from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,FormView,DetailView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from engineer_recuiting.department.models import CreateDepartmentForm,DepartmentProfile,RecruitmentInformation,DeniedReasonForm
from engineer_recuiting.company.models import CompanyProfile



# Create your views here.
'''
we still need decorator function for check is company approved,and if user is a company actor

and the decorator only be put in the view or the function, in 1.9, we can put it on the head of class

'''

class ShowCompanyView(TemplateView):

    template_name = 'company_homepage.html'

    def get_context_data(self, **kwargs):

        user_id=self.request.user.id
        context=super(ShowCompanyView,self).get_context_data(**kwargs)
        context['department']=DepartmentProfile.objects.filter(company__id=user_id)
        context['waiting_recruitment_info']=RecruitmentInformation.objects.filter(status='w')
        return context

    def post(self,req,*args,**kwargs):

        return HttpResponseRedirect('suceesee')

class CreateDepartmentView(FormView):

    form_class = CreateDepartmentForm
    success_url = '/success create department'
    template_name = 'create_department.html'
    department_exist=False

    def get_context_data(self, **kwargs):

        context = super(CreateDepartmentView, self).get_context_data(**kwargs)
        context['department_exist'] = self.department_exist
        context['form']=self.form_class()
        return context

    def form_valid(self, form):

        user=User.objects.get(id=self.request.user.id)
        form=CreateDepartmentForm(self.request.POST)
        instance=form.save(commit=False)
        sub_user_name=user.username+'_'+self.request.POST['department_name']
        sub_user_password=self.request.POST['password']
        email=self.request.POST['email']

        with transaction.atomic():

            User.objects.create_user(username=sub_user_name,password=sub_user_password,email=email)
            sub_user = authenticate(username=sub_user_name, password=sub_user_password)

            if not sub_user:
                self.department_exist=True
                return render(self.request,self.template_name,self.get_context_data())
            instance.user=sub_user
            instance.company=user
            instance.save()

        return super(CreateDepartmentView, self).form_valid(form)

class CompanyDetailView(DetailView):

    model = CompanyProfile
    context_object_name = 'company'

    def get_context_data(self, **kwargs):

        context=super(CompanyDetailView,self).get_context_data()
        user=User.objects.get(id=self.request.user.id)
        context['departments']=user.departments.all()
        return context
@login_required
def change_recruiment_status(req,recruitment_id,way):

    user=req.user
    recruitment_id=int(recruitment_id)

    recruitment=get_object_or_404(RecruitmentInformation,id=recruitment_id)
    if recruitment.department.departmentprofile.company != user:
        return HttpResponseRedirect('hacker')
    if way=='approve':
        recruitment.status='a'
        recruitment.save()
        return HttpResponseRedirect('/success')
    else:
        recruitment.status='d'
        recruitment.save()
        id=recruitment.id
        return render(req,'deny_recruitment_page.html',{'id':id,'falg':True})#if flag =true the don't show the form

class DeniedReasonView(UpdateView):

    form_class = DeniedReasonForm
    model = RecruitmentInformation
    success_url = '/seccess!'
    template_name = 'create_recruitment.html'

