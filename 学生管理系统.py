# -*- coding:utf-8 -*-
stu = []
student = {}


def print_page():
    page = """
    ====================================================
    ❀❀欢迎召唤师来到英雄联盟❀❀
    💗1.添加学生
    💗2.查看学生
    💗3.修改学生信息
    💗4.删除学生
    💗5.返回
    ====================================================
    """
    print(page)


def produceid():
    stu_id = 1
    while True:
        yield stu_id
        stu_id += 1


def add(stu, stuid):
    student.clear()
    name1 = input('请输入姓名：')
    age = int(input('请输入年龄：'))
    tel = input('请输入学生电话：')
    stuid = 'stu' + str(stuid).zfill(3)
    student.update([['学号', stuid], ['姓名', name1], ['年龄', age], ['电话', tel]])
    stud = student.copy()
    stu.append(stud)
    return stu


def lookall(stu):
    for index in range(len(stu)):
        for key in stu[index]:
            print(key, stu[index][key], end='\t')
            print()


def lookname(stu):
    name = input('请输入姓名：')
    for index in range(len(stu)):
        for key in stu[index]:
            if name == stu[index][key]:
                print(key, stu[index][key], end='\t')
                print()


def lookid(stu):
    stuid = input('请输入学号：')
    for index in range(len(stu)):
        for key in stu[index]:
            if stuid == stu[index][key]:
                for key in stu[index]:
                    print(key, stu[index][key], end='\t')
                    print()


def isname(stu1, name):
    for index in range(len(stu1)):
        if name == stu1[index]['姓名']:
            return True
        else:
            return False


def altername(stu1):
    name1 = input('请输入被修改人的姓名:')
    flag = isname(stu1, name1)
    if flag:
        print('1.修改姓名' + '\n' + '2.修改年龄' + '\n' + '3.修改电话')
        num = int(input('请选择1-3'))
        if num == 1:
            name2 = input('请输入你要修改成的姓名:')
            for index in range(len(stu1)):
                if stu1[index]['姓名'] == name1:
                    stu1[index]['姓名'] = name2
        if num == 2:
            age = int(input('请输入要修改成的年龄:'))
            for index in range(len(stu1)):
                if stu1[index]['姓名'] == name1:
                    stu1[index]['年龄'] = age
        if num == 3:
            tel = int(input('请输入要修改成的号码:'))
            for index in range(len(stu1)):
                if stu1[index]['姓名'] == name1:
                    stu1[index]['电话'] = tel
        return stu1


def isid(stu1, stuid):
    for index in range(len(stu1)):
        if stuid == stu1[index]['学号']:
            return True
        else:
            return False


def alterid(stu1):
    stuid = input('请输入被修改人的学号')
    flag = isid(stu1, stuid)
    if flag:
        print('1.修改姓名' + '\n' + '2.修改该年龄' + '\n' + '3.修改电话')
        num = int(input('请选择（1-3'))
        if num == 1:
            name2 = input('请输入你要修改成的姓名')
            for index in range(len(stu1)):
                if stu1[index]['学号'] == stuid:
                    stu1[index]['姓名'] = name2
        if num == 2:
            age = int(input('请输入要修改成的年龄'))
            for index in range(len(stu1)):
                if stu1[index]['学号'] == stuid:
                    stu1[index]['年龄'] = age
        if num == 3:
            tel = int(input('请输入你要修改成的号码'))
            for index in range(len(stu1)):
                if stu1[index]['学号'] == stuid:
                    stu1[index]['电话'] = tel

    return stu1


def delname(stu):
    name1 = input('请输入被删除人的姓名')
    flag = isname(stu, name1)
    if flag:
        for index in range(len(stu)):
            if stu[index]['姓名'] == name1:
                del stu[index]
    return stu


def delid(stu):
    stuid = int(input('请输入被删除人的学号'))
    flag = isid(stu, stuid)
    if flag:
        for index in range(len(stu)):
            if stu[index]['学号'] == stuid:
                del stu[index]
    return stu


stu_id = produceid()
while True:
    print_page()
    num = int(input('请选择(1-5)：'))
    if num == 1:
        while True:
            stuid = next(stu_id)
            stu = add(stu, stuid)
            print('添加成功')
            num1 = int(input('1.继续' + '\n' + '2.返回'))
            if num1 == 1:
                continue
            else:
                break
    elif num == 2:
        while True:
            print('1.查看所有学生' + '\n' + '2.按姓名查找' + '\n' + '3.按学号查找' + '\n' + '4.返回')
            num2 = int(input('请选择（1-4）：'))
            if num2 == 1:
                lookall(stu)
            elif num2 == 2:
                lookname(stu)
            elif num2 == 3:
                lookid(stu)
            else:
                break
    elif num == 3:
        while True:
            print('1.按姓名修改' + '\n' + '2.按学号修改' + '\n' + '3.输出修改后的信息' + '\n' + '返回')
            num3 = int(input('请选择（1-4：'))
            if num3 == 1:
                stu = altername(stu)
            elif num3 == 2:
                stu = alterid(stu)
            elif num3 == 3:
                lookall(stu)
            else:
                break
    elif num == 4:
        while True:
            print('1.按姓名删除' + '\n' + '2.按学号删除' + '\n' + '输出删除后的信息学' + '\n' + '4.返回')
            num3 = int(input('请选择（1-4:'))
            if num3 == 1:
                stu = delname(stu)
            elif num3 == 2:
                stu = delid(stu)
            elif num3 == 3:
                lookall(stu)
            else:
                break
