"""des URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from des.settings import STATIC_ROOT,DAE_FILE_UPLOAD_DIR


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dae/',include('dae.urls',namespace='dae')),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': DAE_FILE_UPLOAD_DIR}),
    # 配置static,解决debug为false时static路径设置无效
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

]


# 全局404页面配置
handler404 = 'dae.views.page_not_found'
# 全局500页面配置
handler500 = 'dae.views.page_error'