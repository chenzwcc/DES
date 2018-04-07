from django.shortcuts import render,render_to_response,HttpResponse
from django.views.generic.base import View
from django import conf
from django.http import FileResponse

import os,time,json
import xlwt,xlrd
from xlutils.copy import copy

from dae import oper_excel
from dae import gener_excel


class DecryptionViews(View):
    """解密"""
    def get(self,request):

        return render(request,'jiemi.html')

    def post(self,request):
        field_str = request.POST.get('text')
        field_list = field_str.split('!')
        field_from_html = []
        for i in field_list:
            if len(i) != 0:
                upload_dir = os.path.join(conf.settings.DAE_FILE_UPLOAD_DIR, str(int(time.time())))
                if not os.path.isdir(upload_dir):
                    os.makedirs(upload_dir)
                file_obj = request.FILES.get('file')
                file_name = os.path.join(upload_dir, file_obj.name)
                with open(file_name, 'wb') as f:
                    for chunks in file_obj.chunks():
                        f.write(chunks)
                if i in oper_excel.getFields(oper_excel.getSheets(file_name)[0]):
                    field_from_html.append(i)
                else:
                    return render(request, 'jiemi.html', {'err_msg': "填写的字段有误"})
        field_dict = {}
        field_from_excel = oper_excel.getFields(oper_excel.getSheets(file_name)[0])
        for i in field_from_html:
            if i in field_from_excel:
                key = oper_excel.one_field_to_Decrydata(file_name,i ,'123456789')
                field_dict[i]=key
        dealed_file=gener_excel.Decrypt_data_to_excel(file_name,field_dict)
        return render(request,'jiemi.html',{'field_str':field_str,'file_name':dealed_file})





class EncryptionViews(View):
    """加密"""
    def get(self,request):
        return render(request, 'jiami.html')

    def post(self, request):
        field_str = request.POST.get('text')
        field_list = field_str.split('!')
        field_from_html = []
        for i in field_list:
            if len(i) != 0:
                upload_dir = os.path.join(conf.settings.DAE_FILE_UPLOAD_DIR, str(int(time.time())))
                if not os.path.isdir(upload_dir):
                    os.makedirs(upload_dir)
                file_obj = request.FILES.get('file')
                file_name = os.path.join(upload_dir, file_obj.name)
                with open(file_name, 'wb') as f:
                    for chunks in file_obj.chunks():
                        f.write(chunks)
                if i in oper_excel.getFields(oper_excel.getSheets(file_name)[0]):
                    field_from_html.append(i)
                else:
                    return render(request, 'jiami.html', {'err_msg': "填写的字段或分隔符有误"})
        field_dict = {}
        field_from_excel = oper_excel.getFields(oper_excel.getSheets(file_name)[0])
        for i in field_from_html:
            if i in field_from_excel:
                key = oper_excel.one_field_to_Encrydata(file_name, i, '123456789')
                field_dict[i] = key
        dealed_file = gener_excel.Encrypted_data_to_excel(file_name, field_dict)

        return render(request, 'jiami.html', dict(field_str=field_str, file_name=dealed_file))

def download(request,file_name):
    file = open(file_name, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/vnd.ms-excel'
    path, file = os.path.split(file_name)

    response['Content-Disposition'] = 'attachment;filename="%s"'%file

    return response



# 404
def page_not_found(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 500
def page_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response

"""处理上传的文件"""
# @csrf_exempt
# def FileUpload(request):
#     if not request.FILES.get('file').name.endswith('.xlsx'):
#         return HttpResponse(json.dumps({"status":False,'err_msg':'The file format must be excel' }))
#     else:
#         upload_dir = os.path.join(conf.settings.DAE_FILE_UPLOAD_DIR,str(int(time.time())))
#         if not os.path.isdir(upload_dir):
#             os.makedirs(upload_dir)
#
#         file_obj=request.FILES.get('file')
#         print(file_obj,type(file_obj))
#         if len(os.listdir(upload_dir))<2:
#             with open(os.path.join(upload_dir,file_obj.name),'wb') as f:
#                 for chunks in file_obj.chunks():
#                     f.write(chunks)
#         else:
#             return HttpResponse(json.dumps({"status":False,'err_msg':'max upload limit is 2' }))
#         return HttpResponse(json.dumps({'status':True}))
#     # f=open(os.path.join('fileupload',file_obj.name),'wb')
#     # for line in file_obj.chunks():
#     #     f.write(line)
#     # table=os.getcwd()+r'\fileupload\\'+file_obj.name
#     # table_list = oper_excel.getSheets(table)
#     # field_list = oper_excel.getFields(table_list[0])
#     # print(field_list)
#     #
#     # return render(request,'jiemi.html',{'len':len(field_list),"field_list":field_list})
