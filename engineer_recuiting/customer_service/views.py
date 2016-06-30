from ipware.ip import get_ip
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,DetailView,TemplateView,UpdateView


from engineer_recuiting.company.models import CompanyProfile
from engineer_recuiting.application.models import Application
from engineer_recuiting.department.models import RecruitmentInformation
from engineer_recuiting.customer_service.models import CompanySearchForm,CompanyAddMoneyForm,ChangeApplicationMoneyForm

# Create your views here.

SUPER_USER_IP='127.0.0.1'
class SuperUserMixin(object):

    def dispatch(self, request, *args, **kwargs):
        ip = get_ip(request)
        if ip != SUPER_USER_IP :
            return HttpResponseRedirect('404')

        return super(SuperUserMixin, self).dispatch(request, *args, **kwargs)


class ShowHomepageView(SuperUserMixin,ListView):

    model = CompanyProfile
    template_name = 'super_user_homepage.html'
    context_object_name = "companies"
    queryset = CompanyProfile.objects.filter(status='W')
    # def get_queryset(self):
    #
    def get_context_data(self, **kwargs):

        context=super(ShowHomepageView,self).get_context_data(**kwargs)
        context['complaints'] = Application.objects.filter(status='c')
        context['form'] = CompanySearchForm()
        return context

class CompanyFullInfoView(SuperUserMixin,DetailView):

    model = CompanyProfile
    template_name = 'company_deatils.html'
    context_object_name = 'company'

class ModifyCompanyStatusView(SuperUserMixin,TemplateView):

    template_name = 'result_of_company_application.html'

    def get(self, request, *args, **kwargs):

        way = kwargs['way']
        id = kwargs['id']

        comany=CompanyProfile.objects.get(id = int(id))

        if way=='1':
            comany.status= 'N'

        else:
            comany.status= 'B'

        comany.save()

        return super(ModifyCompanyStatusView,self).get(request, *args, **kwargs)

class SearchView(SuperUserMixin,ListView):
    template_name = 'company_search_list.html'
    model = CompanyProfile
    context_object_name = 'companies'

    def get_queryset(self):
        form=CompanySearchForm(self.request.GET)
        if form.is_valid():
            name=form.cleaned_data['name']
            print name
        else:
            print form
        # form=form.cleaned_data
        # name = form.get('name')
        # print name
        return CompanyProfile.objects.filter(company_name__contains= name)

class UpdateMoneyForCompanyView(SuperUserMixin,UpdateView):

    form_class = CompanyAddMoneyForm
    model = CompanyProfile
    template_name = 'update_company_money.html'
    success_url = '/send_email_back_to_company!'

class UpdateMoneyForApplication(SuperUserMixin,UpdateView):

    form_class = ChangeApplicationMoneyForm
    model = RecruitmentInformation
    template_name = 'update_recruitment_info.html'
    success_url = '/superuser/add_report_of_complian'




