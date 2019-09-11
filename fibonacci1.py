#! /usr/bin/env python3
# fe斐波那契（Fibonacci）数列，解释：一列数：从1开始，前两项为1，从第三项开始每一项等于前两项之和。推导出公式则为：
#n<3时
#f(n)=1;
#n>2时
#f(n)=f(n-1)+f(n-2)
a, b = 0, 1
while b < 100:
    print (b)
    a, b = b, a + b
