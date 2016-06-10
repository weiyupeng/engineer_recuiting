from django.conf.urls import patterns,include, url
from engineer_recuiting import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from engineer_recuiting.department.views import CreateRecruitmentView,ShowDepartmentView,ModifyRecruitmentView,\
    DeleteRecruitmentView,ShowRecruitmentDetail,DepartmentDetailView


urlpatterns = patterns('engineer_recuiting.department.views',
    url(r'^$',ShowDepartmentView.as_view(),name='show_department'),
    url(r'^create_recruitment$',login_required(CreateRecruitmentView.as_view()),name='create_recruitment'),
    url(r'^modeify_recruitment/(?P<pk>\d+)',login_required(ModifyRecruitmentView.as_view()),name='modify_recruitment_department'),
    url(r'^delete_recruitment/(?P<pk>\d+)',login_required(DeleteRecruitmentView.as_view()),name='delete_recruitment_department'),
    url(r'^change_application_status_id=(?P<app_id>\d+),way=(?P<way>\w+)','changeApplicationStatus',name='department_status_change'),
     url(r'^department_card_id/(?P<pk>\d+)/',DepartmentDetailView.as_view(),name='department_bussiness_card'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)