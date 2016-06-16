
from datetime import datetime
from django.contrib.auth.models import User
from django.views.generic import DetailView,FormView,ListView
from engineer_recuiting.application.models import Application,ApplicationCreateForm
from engineer_recuiting.department.models import RecruitmentInformation,DepartmentProfile
# Create your views here.

'''

this view is responsible for anything concern about the application.which application means after engineer
submit their application, it will be stored by application form, and the application can be a contract or an history
transaction baesd on the different status

this view includes any operation about application , CRUD....

'''

class CreateApplicationView(FormView):
    form_class = ApplicationCreateForm
    success_url = 'success'
    template_name = 'create_application.html'

    def form_valid(self, form):

        recuitment_id=int(self.args[0])
        recuitment=RecruitmentInformation.objects.get(id=recuitment_id)
        user=User.objects.get(id=self.request.user.id)
        instance=form.save(commit=False)
        instance.recruitment=recuitment
        instance.date=datetime.today()
        instance.applier=user
        instance.save()

        return super(CreateApplicationView, self).form_valid(form)

class ApplicationDetailView(DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'appliaction_detail.html'

    def get_context_data(self, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        content=super(ApplicationDetailView,self).get_context_data(**kwargs)
        if hasattr(user,'departmentprofile'):
            content['template']='department'
        if hasattr(user,'engineerprofile'):
            content['template']='engineer'
        if hasattr(user,'companyprofile'):
            content['template']='company'
        return content

class AppliactionHistoryView(ListView):
    template_name ='history.html'
    model = Application
    context_object_name = 'applications'
    def get_queryset(self):
        user=User.objects.get(id=self.request.user.id)
        if hasattr(user,'departmentprofile'):
            return Application.objects.filter(recruitment__department=user).filter(status='f')
        if hasattr(user,'engineerprofile'):
            return Application.objects.filter(applier=user).filter(status='f')
        if hasattr(user,'companyprofile'):
            departments=list(DepartmentProfile.objects.filter(company=user))
            application=Application.objects.all()
            for each in departments:
                application.filter(recruitment__status=departments.user)
            return application


def applicationStatusChange(application,status):
    application.status=status
    return True


