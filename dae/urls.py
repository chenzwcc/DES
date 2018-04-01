# -*- coding:utf:8 -*-
__author__ = 'chenzwcc'

from dae.views import DecryptionViews,EncryptionViews,DecryUploadViews
from django.conf.urls import url

urlpatterns = [
    url(r'^decry/$',DecryptionViews.as_view(),name='decry'),
    url(r'^decry/upload$', DecryUploadViews.as_view(), name='decry'),#解密
    url(r'^encry/$',EncryptionViews.as_view(),name='encry'),  #加密
]