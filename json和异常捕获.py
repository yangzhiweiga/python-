# -*- coding:utf-8 -*-
import json

# loads将json数据转化成python数据
py1 = json.loads('"abc"')
py2 = json.loads('[100,200,true,"Hello",null]')
print(py1, py2)
py3 = json.loads('100')
print(py3)
py4 = json.loads('{"a":1,"b":[1,2],"c":3}')
print(py4)
f = None
# try:
#     with open('data.json', encoding='utf-8') as f:
#         for content in f:
#             print(content)
# finally:
#     f.close()

# dumps将python数据转换成json数据
js1 = json.dumps(100)
print(js1, type(js1))
js2 = json.dumps((10, 'abc', True))
print(js2, type(js2))
js3 = json.dumps([100, 'aaa', None])
print(js3, type(js3))
js4 = json.dumps({'a': 10, 'b': None, 'c': ['a', 'b']})
print(js4, type(js4))

print('======================')
# load 将文件对象中的数据读出来并且转换成python对应的数据
# dump 将python数据转换成json格式的字符串,再写入文件对象中
try:
    with open('data.json', encoding='utf-8') as f:
        content = json.load(f)
        print(content, type(content))  # ['a', 'b', 'c'] <class 'list'>
finally:
    f.close()

# try:
#     # 自己实现dump方法
#     def my_dump(obj, file):
#         with open(file, 'w', encoding='utf-8') as f:
#             strstr = json.dumps(obj)
#             f.write(strstr)
#
#
#     my_dump(['a', 'b', 'c'], 'data.json')  # [”a“, “b“, “c“]
# finally:
#     f.close()

# 异常捕获

# 捕获所有异常
try:
    print([1, 2][0])
    print([1, 2][5])
except:
    print('出现异常')

# 捕获指定异常
try:
    print([1, 2][5])
    print(int('abc'))
    print('+++++++++++')
except IndexError:
    print('下标越界')

# 同时捕获多个异常对不同的异常做出不同的反应
try:
    print([1, 2][5])  # IndexError
    print(int('abc'))  # ValueError
    print({'a': 1}['b'])  # KeyError
except (IndexError, KeyError, ValueError, FileNotFoundError, StopIteration):
    print('出现多个异常中的一种')

# 同时捕获多个异常,对不同的异常做出不同的反应
try:
    print([1, 2][5])  # IndexError
    print(int('abc'))  # ValueError
    print({'a': 1}['b'])  # KeyError
except IndexError:
    print('下标越界')
except KeyError:
    print('键越界')
except ValueError:
    print('值错误')

# try-except-finally(不管代码是否出现异常,也不管异常是否能够捕获到,finally后面的代码段都会执行
try:
    print([1, 2][1])
except ValueError:
    print('值错误')
finally:
    print('不管一场是否捕获到都会执行这段代码')
# 什么时候使用异常捕获：明明知道这段代码可能会出现异常但是有没有办法避免就是用异常捕获
while True:
    try:
        score = float(input('请输入成绩:'))
        break
    except ValueError:
        print('输入有误！请输入数字')


def txt(obj):
    f = None
    try:
        with open(obj, 'r', encoding='utf-8') as f:
            cont = f.read()
        return cont
    except FileNotFoundError:
        print('文件路径有误')
        return ''
    finally:
        # python不支持传统的三元运算 可以用 x=x+1 if x%2==1 else x代替 为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）
        f.close() if f else None


print(txt('data.json'))

# 抛出异常(语法：raise 错误类型-程序执行到raise语句的时候直接抛出异常并崩溃)
try:
    age = int(input('请输入年龄：'))
    if not 0 <= age <= 100:
        raise IndexError
except:
    print('输入有误')

# 练习
file = ''
try:
    with open('message.json', 'r', encoding='utf-8') as f:
        file = f.read()
except FileNotFoundError:
    print('文件路径不存在,自动为你新增该文件')
    with open('message.json', 'w', encoding='utf-8') as f:
        f.write('')
finally:
    f.close()

if file:
    add_list = json.loads(file)
else:
    add_list = []

while True:
    print('1.添加' + '\n' + '2.返回')
    num = int(input('请输入1-2：'))
    stu = {}
    if num == 1:
        stu.clear()
        name = input('请输入添加的姓名')
        age = input('请输入添加的年龄:')
        tel = input('请输入添加的电话')

        while True:
            if not name:
                name = input('请输入添加的姓名')
            elif not age:
                age = input('请输入添加的年龄:')
            elif not tel:
                tel = input('请输入添加的电话')
            else:
                break

        stu = {'name': name, 'age': age, 'tel': tel}
        add_list.append(stu)
    else:
        break

content = json.dumps(add_list)
try:
    with open('message.json', 'w', encoding='utf-8') as f:
        f.write(content)
finally:
    f.close()

try:
    with open('message.json', encoding='utf-8') as f:
        file = f.read()
finally:
    f.close()
print(file)
