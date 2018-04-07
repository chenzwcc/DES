# -*- coding:utf:8 -*-
__author__ = 'chenzwcc'

from dae import views
from django.conf.urls import url

urlpatterns = [
    url(r'^decry/$',views.DecryptionViews.as_view(),name='decry'),  #解密

    url(r'^encry/$',views.EncryptionViews.as_view(),name='encry'),  #加密

    url(r'^download/(?P<file_name>[\w\W]*)/$',views.download,name='download')
]
