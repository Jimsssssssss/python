#! /usr/bin/env python3
# 输入学生的人数，课程数，求和，判断和的大小
n = int(input("请输入班级人数 "))
data = {} # 用来存放名字对应的成绩
Objects=("physics","match","history")
for i in range(0, n):
    name = input("请输入学生的姓名：")
    marks = [] #存放对应科目的成绩
    for x in Objects:
        marks.append(int(input('Enter marks of {}: '.format(x))))
    data[name]=marks
for x, y in data.items():
    total =  sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed")
    else:
        print(x, "passed :)")
