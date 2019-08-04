# -*- coding:utf-8 -*-
import random

print('abc\u4f59123')
str1 = 'qwerqerut'
print(str1[0:9:3], str1[::-1])

str1 = '123'
new_str1 = str1.center(7, '*')  # **123**
new_str2 = str1.ljust(7, '*')  # 123****
new_str3 = str1.rjust(7, '*')  # ****123
new_str4 = str1.zfill(7)  # 0000123
print(new_str1, new_str2, new_str3, new_str4)

num = random.randint(0, 99)
new_num = 'python1818' + str(num).rjust(7, '0')
print(new_num)

str = 'asdfadsfadsfasdfadsf'
str1 = 'a'
print(str.count(str1))
print(str.endswith('a'))
print(str.startswith('a'))

exp = 'yangzhiwei   '
print(exp.expandtabs(tabsize=2))
print(exp.find('g'))
num = '44564564564'
print(num.isdigit())
print(exp.isalpha())

str1 = '123';
str2 = 'a#*&'
print(str1.join(str2))
print(exp.upper())
print(str2.rstrip('&'))
print(exp.replace('yang','Yang'))
print(exp.split('a'))
