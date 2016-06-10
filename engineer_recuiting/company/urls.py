from django.conf.urls import patterns,include, url
from engineer_recuiting import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from engineer_recuiting.company.views import ShowCompanyView,CreateDepartmentView,CompanyDetailView,DeniedReasonView
from engineer_recuiting.department.views import ShowRecruitmentDetail

urlpatterns = patterns('engineer_recuiting.company.views',
    url(r'^$',login_required(ShowCompanyView.as_view())),
    url(r'^create_department$',login_required(CreateDepartmentView.as_view()),name='create_department'),
    url(r'^bussiness_card_id/(?P<pk>\d+)/',CompanyDetailView.as_view(template_name ='company_business_card.html'),name='compamy_bussiness_card'),
    url(r'^modify_recruitment_id=(\d+)_way=(\S+)','change_recruiment_status',name='company_change_recruiment_status'),
    url(r'^add_the_reason_of_deny/(?P<pk>\d+)',login_required(DeniedReasonView.as_view()),name='add_the_reason_of_deny'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)