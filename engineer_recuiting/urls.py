"""engineer_recuiting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from engineer_recuiting.department.views import ShowRecruitmentDetail
from engineer_recuiting.application.views import ApplicationDetailView

from engineer_recuiting import settings

urlpatterns = [
    url(r'^$','engineer_recuiting.authenticating.views.log_in',name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_user_(\w+)','engineer_recuiting.authenticating.views.create_user'),
    url(r'^logout','engineer_recuiting.authenticating.views.all_logout',name='logout'),
    url(r'^engineer/',include('engineer_recuiting.engineer.urls')),
    url(r'^company/',include('engineer_recuiting.company.urls')),
    url(r'^department/',include('engineer_recuiting.department.urls')),
    url(r'^application/',include('engineer_recuiting.application.urls')),
    url(r'^message/',include('engineer_recuiting.message.urls')),
    url(r'^comments/',include('engineer_recuiting.comment.urls')),
    url(r'superuser/',include('engineer_recuiting.customer_service.urls')),
    url(r'^recuirtment_detail/(?P<pk>\d+)/$',login_required(ShowRecruitmentDetail.as_view()),name='recuirtment_detail'),
    url(r'^application_detail/(?P<pk>\d+)/$',login_required(ApplicationDetailView.as_view()),name='application_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
