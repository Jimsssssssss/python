#! /usr/bin/env python3
# 十以内的乘法表
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6
x=1
while x<11:
    n=1
    while n<= 10:
        print(x*n, end=" ")
        n += 1;
    print()
    x += 1
