# -*- coding:utf:8 -*-
__author__ = 'chenzwcc'


import xlrd

from dae import pyD


def getSheets(file):
    """得到sheet并返回"""
    workbk = xlrd.open_workbook(file)
    sheets = workbk.sheet_names()
    sheet_cot = []
    for i in range(len(sheets)):
        if workbk.sheet_by_index(i).nrows != 0 and workbk.sheet_by_index(i).ncols != 0:
            sheet_cot.append(workbk.sheet_by_index(i))
    return sheet_cot


def getFields(sheet):
    """得到sheet中的字段名"""
    return sheet.row_values(0)


def getValue(sheet, num):
    """得到对应字段的列值"""
    cols = sheet.col_values(num)
    values_list = []
    for i in range(1, len(cols)):
        values_list.append(str(cols[i]))
    return values_list


def getEncry(values_list, key2):
    """对数据进行加密并返回
     encryed_list:加密后的值"""
    encryed_list = []
    for i in values_list:
        encryed_list.append(pyD.DesEncrypt(i, key2))
    return encryed_list


def getDecy(encryed_list, key2):
    """ 对数据进行解密并返回 decyed_list:解密后的数据"""
    decyed_list = []
    for i in encryed_list:
        decyed_list.append(pyD.DesDecrypt(i, key2))
    return decyed_list


def one_field_to_Decrydata(file_name,field,key):
    """file_name：Excel表格名称
       fields：被操作的字段
       key：密码
       解密
    """
    table_list = getSheets(file_name)
    jie_hou_list=[]
    table = table_list[0]
    field_list = getFields(table)
    num_list = getValue(table, field_list.index(field))
    jie_hou_list.append(getDecy(num_list,key))
    return jie_hou_list

def one_field_to_Encrydata(file_name,field,key):
    """file_name：Excel表格名称
       fields_list：被操作的字段
       key：密码
       加密
    """
    table_list = getSheets(file_name)
    num_list = []
    jia_hou_list=[]
    for i in table_list:
        field_list = getFields(i)
        num_list = getValue(i, field_list.index(field))
    jia_hou_list.append(getEncry(num_list,key))
    return jia_hou_list

