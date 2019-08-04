# -*- coding:utf-8 -*-
import random

age = random.randint(0, 100)
if age > 18:
    print('成年')

if age > 60:
    print('老年')
elif age > 30:
    print('中年')
else:
    print('青年')

str1 = 'Asfer'
if str1[0].isalpha():
    if str1[0].isupper():
        print('大写字母')

for _ in range(5):
    print('**')

index = 0
while index < len(str1):
    print(str1[index])
    index += 1
else:
    print('end')
