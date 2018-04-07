# -*- coding:utf:8 -*-
__author__ = 'chenzwcc'




import xlrd
from xlutils.copy import copy
from dae.oper_excel import getSheets,getFields
import os


def Encrypted_data_to_excel(file_name,dic):
    """加密后的数据保存到表"""
    workbook = xlrd.open_workbook(file_name)
    wbn = copy(workbook)
    ws = wbn.get_sheet(0)
    fields_list = getFields(getSheets(file_name)[0])
    for j in dic.keys():
        for i in range(1,len(dic[j][0])+1):
            value = str(dic[j][0][i - 1])
            ws.write(i, fields_list.index(j), value)
    path,file=os.path.split(file_name)
    dealed_file = path+'\\加密的'+file
    wbn.save(dealed_file)
    return dealed_file


def Decrypt_data_to_excel(file_name,dic):
    """解密后的数据保存到表"""
    workbook = xlrd.open_workbook(file_name)
    wbn = copy(workbook)
    ws = wbn.get_sheet(0)
    fields_list = getFields(getSheets(file_name)[0])
    for j in dic.keys():
        for i in range(1,len(dic[j][0])+1):
            ws.write(i, fields_list.index(j), str(dic[j][0][i - 1]))
    path,file=os.path.split(file_name)
    dealed_file = path + '\\解密' + file
    wbn.save(dealed_file)
    return dealed_file
