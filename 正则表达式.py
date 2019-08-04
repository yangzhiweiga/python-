# -*- coding:utf-8 -*-
import re

# 普通字符串 匹配本身
re_str = r'abc'
result = re.fullmatch(re_str, 'abc')
print(result)
# 匹配任意字符 一个.只能匹配一个字符
re_str = r'a.c'
result = re.fullmatch(re_str, 'abc')
print(result)
# \w匹配字母数字或下划线
# 匹配一个长度是5的字符串并且字符串的前两位是数字字母或者下划线后面是三个任意字符串 \w中文也能匹配
re_str = r'\w\w...'
result = re.fullmatch(re_str, '_a123')
print(result)
# \s匹配空白字符
# 空白字符串包括空格,制表符,换行符:\t,\r,\n
re_str = r'\w\w\s\w'
result = re.fullmatch(re_str, 'hj\t8')
print(result)
# \d匹配数字字符
re_str = r'\d\d\d..'
result = re.fullmatch(re_str, '082ww')
print(result)
# \b检测单词边界
re_str = r'hello\bworld'
result = re.fullmatch(re_str, 'hello world')
print(result)
re_str = r'\bhello，\bworld'
result = re.fullmatch(re_str, 'hello，world')
print(result)
# ^检测字符串开头
re_str = r'^The..'
result = re.fullmatch(re_str, 'The2;')
print(result)
# $检测字符串结尾
re_str = r'The$'
result = re.fullmatch(re_str, 'The')
print(result)
