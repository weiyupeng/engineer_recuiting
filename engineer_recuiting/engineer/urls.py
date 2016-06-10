from django.conf.urls import patterns,include, url
from engineer_recuiting import settings
from django.conf.urls.static import static
from engineer_recuiting.engineer.views import EngineerprofileView,SearchingResulteView

urlpatterns = patterns('engineer_recuiting.engineer.views',
    url(r'^$','show'),
    url(r'^email_confirm_email=(\S+),id=(\d+)$','conform_email'),
    url(r'^my_info_(\w*)','manage_info',name='my_info'),
    url(r'^add_degree','add_degree'),
    url(r'^delete_degree_(\d+)','delete_degree'),
    url(r'^search',SearchingResulteView.as_view(),name='searching'),
    url(r'^business_card_user_id=(\d+)',EngineerprofileView.as_view(),name='business_card'),
    url(r'^change_application_status/(?P<app_id>\d+)/(?P<way>\w+)','changeApplicationStatus',name='change_engineer_application_status')

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)