# -*- coding: utf-8 -*-
# 19

def main2():
    b = []
    x = input("u请输入数据个数:")
    for i in range(x):
        b.append(input("result: "))
    print b
    a = 0
    z = 0
    for j in b:
        if j > 60:
            a += j
        if j > 40:
            z += 1
    print a
    print z
        

main2()
