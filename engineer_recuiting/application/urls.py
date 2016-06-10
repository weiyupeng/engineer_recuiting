from django.conf.urls import patterns,include, url

from django.contrib.auth.decorators import login_required
from engineer_recuiting.application.views import CreateApplicationView,AppliactionHistoryView



urlpatterns = patterns('engineer_recuiting.application.views',
    url(r'^create_application_recuitment_id=(\d+)$',login_required(CreateApplicationView.as_view()),name='create_application'),
    url(r'^review_history',login_required(AppliactionHistoryView.as_view()),name='view_history')

)