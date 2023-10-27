print(
"""计算机随机生成一个六位数，用户需要猜测这个数字。
每次猜测后，程序会给出两个提示：A 和 B。
A 表示用户猜测的数字中有多少位数字与计算机生成的数字相同且位置也相同；
B 表示用户猜测的数字中有多少位数字与计算机生成的数字相同但位置不同。
当用户猜对所有六位数字时，游戏结束。\n""")

import random

def fun(a,b,A):
    for i in range(0,len(a)):
        if a[i] == b[i]:
            A += 1
        else:
            continue
    return A
     
def fun1(a,b,B):
    for i in range(0,len(a)):
        if a[i] == b[i]:
            a = a.replace(a[i],"S")
        for j in range(0,len(b)):
            if b[j] == a[i]:
                B += 1
                a = a.replace(a[i],"S")
            else:
                continue
    return B

while True:
    a = str(random.randint(100000,999999))
    while True:
        try:
            b = input("请输入一个6位数的数字:")
            A = 0
            B = 0
            print(a)
        except:
            print("请输入正确的6位数")
        print(fun(a,b,A),"A",fun1(a,b,B),"B")
        if fun(a,b,A) == 6:
            break
        
    print("下一次")
