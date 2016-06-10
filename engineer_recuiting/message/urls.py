from django.conf.urls import patterns,include, url
from engineer_recuiting.message.views import MessageBoxView,SendMessageView

urlpatterns = patterns('engineer_recuiting.engineer.views',
    url(r'^message_box',MessageBoxView.as_view(),name='show_message_box'),
    url(r'message_senging/(?P<id>\d+)',SendMessageView.as_view(),name='sending_message'),


)