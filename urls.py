from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','weixin.views.home_page',name='index'),
    url(r'^test/','weixin.views.case_request'),
    url(r'^authentication/','weixin.views.authentication'),
    url(r'^case/','weixin.views.case_new'),
    url(r'^case_preview/','weixin.views.case_preview'),
    url(r'^case_submit/','weixin.views.case_submit'),
    url(r'^case_verify/.*','weixin.views.case_verify'),
    url(r'^case_assign/','weixin.views.case_assign'),
    url(r'^case_sendback/','weixin.views.case_sendback'),
    url(r'^idbind/','weixin.views.IdBind'),
    url(r'^idbind_process/','weixin.views.IdBind_process'),
]
