from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


from django.http.response import HttpResponse

class DecryptionViews(View):
    """解密"""
    def get(self,request):
        return render(request,'jiemi.html')

    def post(self,request):
        pass

class DecryUploadViews(View):
    """处理上传的文件"""

    @csrf_exempt
    def post(self,request):
        return HttpResponse("上传成功")

class EncryptionViews(View):
    """加密"""
    def get(self,request):
        pass

    def post(self,request):
        pass

