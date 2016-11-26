# -*- coding: utf-8 -*-
# 字母转换Ascii

str = input('Enter your convert english:\n')
asc_list = [ord(i) for i in str]
bin_list = [bin(i)[2:] for i in asc_list]
oct_list = [oct(i)[2:] for i in asc_list]
hex_list = [hex(i)[2:] for i in asc_list]

print('转换后结果：\nascii：{}\n二进制：{}\n十进制：{}\n十六进制：{}'.format(asc_list, bin_list, oct_list, hex_list))