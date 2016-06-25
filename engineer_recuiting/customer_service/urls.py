from django.conf.urls import patterns,include, url
from django.conf.urls.static import static

from engineer_recuiting import settings
from engineer_recuiting.customer_service.views import ShowHomepageView,CompanyFullInfoView,ModifyCompanyStatusView,\
    SearchView,UpdateMoneyForCompanyView,UpdateMoneyForApplication


urlpatterns = patterns('engineer_recuiting.company.views',
    url(r'^$',ShowHomepageView.as_view()),
    url(r'^company_details/id=(?P<pk>\d+)',CompanyFullInfoView.as_view(),name='show_company_detail'),
    url(r'^modify_company_status/id=(?P<id>\d+)/way=(?P<way>\d)',ModifyCompanyStatusView.as_view(),name='modify_company_status'),
    url(r'^search_company',SearchView.as_view(),name='search_company'),
    url(r'^update_money_for_comapny/id=(?P<pk>\d+)',UpdateMoneyForCompanyView.as_view(),name='update_money'),
    url(r'^deal_with_complain/id=(?P<pk>\d+)',UpdateMoneyForApplication.as_view(),name='handle_complain'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)