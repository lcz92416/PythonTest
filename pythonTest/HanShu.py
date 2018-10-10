import math
import os
import sys
def printme( str ):
    "函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明"
    print(str)
    return

def ChangeInt( b ):
    print("222")

b = 2
ChangeInt(b)
print(b) # 结果是 2
printme(str="123")
name="全局变量"
def printinfo( name, age = 35 , *asd):
    "默认值，不定长参数"
    print("Name: ", name)
    print("Age ", age)
    for var in asd:
        print("asd ", var)
    return

printinfo("li",2,3,4,56,)

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum( 10, 20 ))

Money = 2000
def AddMoney():
    # 全局变量:
    global Money
    Money = Money + 1
print(Money)
AddMoney()
print(Money)

#返回的列表容纳了在一个模块里定义的所有模块，变量和函数
content = dir(math)
print(content)
print(__name__)
