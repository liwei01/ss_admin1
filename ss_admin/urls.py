# -*- coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from ss import views as ss_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ss_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$' , ss_views.index),
    url(r'^index' , ss_views.index),



    url(r'^ss/product' , ss_views.Prod),
    url(r'^ss/user' , ss_views.user),
    url(r'^ss/node' , ss_views.node),
    url(r'^ss/myinfo' , ss_views.myinfo),
    url(r'^ss/prder',ss_views.prder),
    url(r'^ss/create_prder',ss_views.create_prder),

    url(r'^ss/login',ss_views.login),
    url(r'^ss/logout',ss_views.logout),
   # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
   # url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    #用户注册
    url(r'^ss/register',ss_views.register),

    #生成二维码   http://127.0.0.1:8000/qrcode/http://www.baidu.com
    url(r'^qrcode/(.+)$', ss_views.generate_qrcode, name='qrcode'),
]
