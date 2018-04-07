# -*- coding:utf:8 -*-
__author__ = 'chenzwcc'

from pyDes import *

import base64
# Des CBC
# 自定IV向量
Des_IV = b"\xef\xab\x56\x78\x90\x34\xcd\x12"
def DesEncrypt(str1,key):
    # str 明文password
    # key uid
    Des_Key = (key+"0000")[0:8]
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
    str1=bytes(str1,'utf8')
    EncryptStr = k.encrypt(str1)
    return base64.b64encode(EncryptStr) #转base64编码返回


def DesDecrypt(str2,key):
    # str 密文password
    # key uid
    Des_Key = (key+"0000")[0:8]
    EncryptStr = base64.b64decode(str2[2:-1])
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
    DecryptStr = k.decrypt(EncryptStr)
    return DecryptStr.decode('utf8')


if __name__ == "__main__":
    print(DesEncrypt('123.456','123456789'),len(DesEncrypt('呼和浩','123456789')))

    # print(DesDecrypt(b'\\x1e\\xe8\\xfe,\\x92P\\\\\\xcf','123456789'))
    print(DesDecrypt("b'Huj+LJJQXM8='",'123456789'))
