from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required
from engineer_recuiting.comment.views import DepartmentCommentView,EngineerCommentView



urlpatterns = patterns('engineer_recuiting.application.views',
    url(r'^create_engineer_comments/(?P<pk>\d+)',login_required(EngineerCommentView.as_view()),name='create_engineer_comment'),
    url(r'^create_department_comments/(?P<pk>\d+)',login_required(DepartmentCommentView.as_view()),name='create_departments_comment')

)