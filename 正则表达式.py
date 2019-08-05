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
# \大写字母对应的功能是\小写字母功能取反
# \W 匹配非字母数字下划线
# \D 匹配非数字字符
# \S 匹配空白字符串
# \B 检测非单词边界
re_str = r'\d\D\s\s\Ba'
print(re.fullmatch(re_str, '2a  a'))
# 字符集
# 匹配中括号出现的任意一个字符
re_str = r'\d[bcd]'
result = re.fullmatch(re_str, '2d')
print(result)
# [a-z] 表示匹配所有的小写字母
# [A_Z] 表示匹配所有的大写字母
# [a-zA-Z] 匹配所有的字母
# [1-7] 匹配数字字符1到7
# [\u4e00-\u9fa5] 匹配所有的中文
# [字符1字符2-] 这儿的-表示减号本身
re_str = r'[1-7][abc-][a-z]'
result = re.fullmatch(re_str, '3-b')
print(result)
# [^abc] 匹配不再abc以外的任意一个字符
# [^\d] 匹配除了数字字符以外的任意一个字符
# [^a-z] 匹配除了小写字母以外的其他任意一个字符
# [abc^] 匹配abc^中的任意一个字符
re_str = r'[^a-z]'
result = re.fullmatch(re_str, '是')
print(result)
# 正则控制匹配次数
# *(匹配0次或者多次) a* a出现0次或多次 \d* 任意数字出现0次或多次 [abc]* a,b,c出现0次或多次 [A-F] A到F中任意字符出现0次或多次
print(re.fullmatch(r'a*b', 'b'))
# +(匹配1次或者多次)
print(re.fullmatch(r'a+b', 'aaaab'))
# ?(匹配0次或1次)
print(re.fullmatch(r'[+-]?[1-9]\d*', '+145345'))
# {N} 匹配N次 a{3} 匹配三个a
# {M,N}} 匹配M到N次
# {,N} 最多匹配N次
# {M,} 至少匹配M次
re_str = r'[a-zA-Z][a-zA-Z\d]{5,11}'
# str1 = input('请输入密码:')
str1 = 'ab123456'
result = re.fullmatch(re_str, str1)
if result:
    print('密码正确')
else:
    print('密码错误')

# 分之、捕获、贪婪
# 分之 条件1|条件2 匹配条件1或条件2
# \d{2}|[a-z] 匹配两个数字字符或者一个小写字母
# 正则中的分之也会出现短路，当条件1可以匹配就不会在使用条件2匹配
re_str = r'[-+]?[1-9]\d*[.]?\d*|[-+]?0[.][0-9]*[1-9]|0'
result = re.fullmatch(re_str, '0.0000009')
print(result)
# 捕获 通过正则获取符合条件的字串的时候可以在正则表达式中加括号，匹配后之获取括号里面匹配到的内容
# re.findall(正则表达式,字符串) 在字符串中获取符合正则表达式条件的所有的字串返回一个列表
str1 = 'ahs123+34asdf24'
print(re.findall(r'\d+', str1))

str2 = 'a153s123+34asfa24'
print(re.findall(r'a\d+', str2))
print(re.findall(r'a(\d+)', str2))

str3 = 'http://www.qq.com'
print(re.findall(r'^(http://)?www.(\w+).com', str3))
# 重复匹配 带多个分组的正则表达式可以在分组的后面通过添加\数字来重复前面第几个分组中匹配到的内容
re_str = r'(\d{3})([a-z]{2})a\1{2}-\2'
print(re.findall(re_str, '123efa123123-ef'))
# 贪婪 匹配次数后加？就是贪婪匹配：*?,+?,??,{M,N}?,{M,}?表示尽可能少的重复
re_str = 'a.+b'
re_str1 = 'a.+?b'
str1 = 'xxahdjbnnkhasssbkkkkk'
print(re.findall(re_str, str1))
print(re.findall(re_str1, str1))
# 转义字符 \
re_str = r'a\+\(\d{2}\)'
print(re.fullmatch(re_str, 'a+(23)'))
# re模块
# complie
re_str = r'\d{3}'
re_obj = re.compile(re_str)
print(re_obj.fullmatch('234'))
# match 不完全匹配之匹配字符串开头 之匹配字符串开头 匹配成功返回匹配对象匹配失败返回None
# fullmatch 完全匹配从字符串开头匹配到字符串结束
re_str = r'\d([A-Z]{2})'
result = re.fullmatch(re_str, '2HKdfsd')
print(result)
result = re.match(re_str, '8KLsifdfd==')
print(result)
# 匹配对象
# start,end 获取匹配结果的开始下标和结束下标
# 匹配对象.start(n)/匹配对象.end(n) 获取正则表达式中第n个分组匹配到的开始下标/结束下标
print(result.start(), result.end())
# print(result.start(1), result.end(2))
# ggroup 获取匹配到的内容
# 匹配对象.group() 获取整个正则表达式匹配到的内容
# 匹配对象.group(n) 获取正则表达式第n个分组匹配到的内容
print(result.group())
print(result.group(1))
# string 获取匹配的原字符串
# 匹配对象.string
print(result.string)
# search
# search(正则表达式,字符串)匹配字符串中第一个满足正则表达式的字串，如果匹配成功返回匹配对象否则返回None
str1 = 'abc123hks362shjjk990kll'
result = re.search(r'\d{3}[a-z]{2}', str1)
print(result)
# split split(正则表达式,字符串) 在字符串中按照满足正则表达式条件的字串对字符串进行切割
str1 = 'ab+c7hdjd8jss-sk9s9kk*k'
result = re.split(r'\d+|[+*-]+', str1)
print(result)
# findall findall(正则表达式,字符串) 在字符串中获取满足正则表达式的所有的字符返回一个列表列表元素是字符串
str = 'abcd1235asdf'
result = re.findall(r'a[a-zA-Z]+', str)
print(result)


# finditer finditer(正则表达式，字符串) 获取字符串中满足正则表达式的内容返回的是一个迭代器
# def yt_finditer(pattern, string):
#     re1 = re.search(pattern, string)
#     while re1:
#         yield re1
#         string = string[re1.end():]
#         re1 = re.search(pattern, string)
#
# str1='haja37jjkd89sdhs909nnna238==='
# result = yt_finditer(r'[a-zA-Z]{2,}(\d+)(a-z)+?', str1)
# print(next(result))
