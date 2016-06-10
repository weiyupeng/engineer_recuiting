from datetime import datetime


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,FormView,DetailView,UpdateView,DeleteView
from django.http import HttpResponseRedirect
from django.db import transaction
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

from engineer_recuiting.department.models import CreateRecruitmentForm,RecruitmentInformation
from engineer_recuiting.application.models import Application
from engineer_recuiting.application.views import applicationStatusChange
from engineer_recuiting.department.models import DepartmentProfile
from engineer_recuiting.comment.models import Comment

# Create your views here.
'''
we still need decorator function for check if company approved,and if user is a company actor

and the decorator only be put in the view or the function, in 1.9, we can put it on the head of class

we can use the permission to handl this see the link http://stackoverflow.com/questions/4778685/how-do-i-use-django-groups-and-permissions

Override dispatch to apply the permission decorator

and we still need a decorator to determine if a company has auth to change this applications stuatus
'''
class ShowDepartmentView(TemplateView):

    template_name ='department_homepage.html'


    def get_context_data(self, **kwargs):

        context=super(ShowDepartmentView,self).get_context_data(**kwargs)
        user_id=self.request.user.id
        #get the recruiting info and classify it
        recruiting=RecruitmentInformation.objects.filter(department__id=user_id)
        approved_recruiting=recruiting.filter(status='a')
        denied_recruiting=recruiting.filter(status='d')
        waited_recruiting=recruiting.filter(status='w')
        applications=Application.objects.filter(recruitment__department__id=user_id,recruitment__status='a')
        context['approved_recruiting']=approved_recruiting
        context['denied_recruiting']=denied_recruiting
        context['waited_recruiting']=waited_recruiting
        context['applying_application']=applications.filter(status='w').exclude(recruitment__status='e')
        context['waiting_feed_back_application']=applications.filter(status='a').exclude(recruitment__status='e')
        context['processing_application']=applications.filter(status='s')
        return context
'''we also need a business_card for department'''
class DepartmentDetailView(DetailView):
    model = DepartmentProfile
    context_object_name = 'department'
    template_name = 'department_detail.html'
class CreateRecruitmentView(FormView):

    form_class = CreateRecruitmentForm
    success_url = '/success create recruiment'
    template_name = 'create_recruitment.html'


    def form_valid(self, form):

        user=User.objects.get(id=self.request.user.id)
        form=CreateRecruitmentForm(self.request.POST)
        instance=form.save(commit=False)
        instance.department=user

        instance.date=datetime.today().date()

        instance.save()

        return super(CreateRecruitmentView, self).form_valid(form)

class ModifyRecruitmentView(UpdateView):

    form_class = CreateRecruitmentForm
    model = RecruitmentInformation
    success_url = '/seccess!'
    # template_name_suffix = '_update_form' still don't get it
    template_name = 'create_recruitment.html'

class DeleteRecruitmentView(DeleteView):

    model = RecruitmentInformation
    context_object_name = 'Recruitment'
    template_name = 'recruitmentinformation_confirm_delete.html'
    success_url = reverse_lazy('show_department')

class ShowRecruitmentDetail(DetailView):

    model = RecruitmentInformation
    context_object_name = 'recruitment_info'
    template_name ='recruitment_detail.html'

    def get_context_data(self, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        content=super(ShowRecruitmentDetail,self).get_context_data(**kwargs)
        if hasattr(user,'departmentprofile'):
            content['template']='department'
        if hasattr(user,'engineerprofile'):
            content['template']='engineer'
        if hasattr(user,'companyprofile'):
            content['template']='company'
        return content
@login_required
    #@ operation_auth_required
def changeApplicationStatus(req,app_id,way):
    application=Application.objects.get(id=int(app_id))
    if way=='approve_application':
        if application.status!='w':
            return HttpResponseRedirect('you cant change it to this stutus')
        application.recruitment.status='e'
        applicationStatusChange(application,'a')
    if way=='deny_application':
        if application.status!='w':
            return HttpResponseRedirect('you cant change it to this stutus')
        application.recruitment.status='a'
        applicationStatusChange(application,'d')
    if way=='finish_application':
        if application.status!='s':
            return HttpResponseRedirect('you cant change it to this stutus')
        Comment.objects.create(application=application)
        applicationStatusChange(application,'f')
    if way=='complain':
        applicationStatusChange(application,'c')
    application.is_department_review=True
    application.save()
    return HttpResponseRedirect('/success~~~~')
        #### we might d other things in here~~~
