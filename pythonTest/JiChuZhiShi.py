import time
import calendar
print('Hello World!');print(200+100);print("Hello World!"+"Hello World!");print("Hello","World!");print("200+100=",200+100)
item_one=1
item_two=2
item_three=3
total = item_one + \
        item_two + \
        item_three
print(total)
to=[1,2,
    3,4]
print(to)
#name=input('please enter your name: \n')
#print("Hello World!",name)
a=b=c=1
a1,b1,c1=1,2,3
print(a,b,c)
print(a1,b1,c1)
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
x="a"
y="b"
# 换行输出
print(x)
print(y)
print('---------')
# 不换行输出---(python 2.x版本中用“,”，3.x中使用“end=""”)
print(x),
print(y),
print(x,end="")
print(y)

# 不换行输出
print(x,y)
#####################################del############################################
print("######################################del########################################")
del a,b,c
str="231"
str=int(str)
print("str",str+1)
del str
print("str",str)
#del删除后 以下语句报错  NameError: name 'a' is not defined
# print("a,b,c",a,b,c)
######################################Number########################################
#Number数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
######################################字符串########################################
print("######################################字符串########################################")
s = 'abcdef'
#包含头不包含尾
print(s[1:5]);print(s[:5]);print(s[:]);print(s[-4:-2])
#引号前小写的"u"表示这里创建的是一个 Unicode 字符串
u'Hello\u0020World !'
#三引号为注释，双引号单引号都是，可换行
abc="""第一行
第二行"""
print(abc)
#格式化|%s格式化字符串、%d格式化整数
print ("My name is %s and weight is %d kg!" % ('Zara', 21))
#三引号可包含特殊字符
#补空格
"abc".rjust(5)
#str.format()
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
######################################列表########################################
print("######################################列表########################################")
#有序
tuple =["a",1,'b',2,3.3,3e+26J]
tinylist = [123, 'john']
print(tuple[0]);print(tuple);print(tuple[1:3]);print(tuple*2);print(tuple+tinylist)
var1=tuple.pop(1)
tinylist.append(var1)
print(tuple[0]);print(tuple);print(tuple[1:3]);print(tuple*2);print(tuple+tinylist)
list=["1","2",3,"4","5",6,"7","8"]
print(len(list),list)
list.remove("4")
print(len(list),list)
list.pop(4)
print(len(list),list)
del list[4]
print(len(list),list)
######################################元组########################################
print("######################################元组########################################")
#不能二次赋值，相当于只读列表，只可以用del删除整个元组
tuple =("a",1,'b',2,3.3,3e+26J)
tinylist = (123, 'john')
print(tuple[0]);print(tuple);print(tuple[1:3]);print(tuple*2);print(tuple+tinylist)
tup1 = ()
print(tup1)
tup1 = (50,)
print(tup1)
tup1=(100)
print(tup1)

tup2=(1,2,3)
print(tup2)
#可以
tup2=(2,2,2)
#出错
#tup2[0]=3
######################################字典########################################
print("######################################字典########################################")
#无序，键不可变，故只能由数字，字符串或元组构成
dict={}
dict[abc]="aabbcc"
dict["abc"]="aa1bb1cc1"
dict[1]=1
tinydict = {'a': '1','b':2, 'c': '3'}
print(dict['abc'])
print(dict[abc])
print(dict[1])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
# 删除键是'Name'的条目
del dict['abc']
# 清空词典所有条目
dict.clear()
# 删除词典
del dict
######################################集合--无序的不重复元素序列########################################
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
print("######################################集合########################################")
s=set("abcdefg")
print(s)
s.add(1)
print(s)
s.update([2,3])
print(s)
#移除，不存在会报错
s.remove(1)
print(s)
#移除，不存在不会报错
s.discard(2)
s.discard(1)
print(s)
s.clear()
print(s)
######################################成员运算符########################################
print("######################################成员运算符########################################")
#a in list
#a not in list
######################################身份运算符########################################
print("######################################身份运算符########################################")
a="123"
b="123"
if ( a is b ):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")
a=123
b=123
if ( a is not b ):
    print("2 - a 和 b 没有相同的标识")
elif( a == 1 ):
    a=1
else:
    print("2 - a 和 b 有相同的标识")
#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
#a = [1, 2, 3]
#b = a
#b is a
#True
#b == a
#True
#b = a[:]
#b is a
#False
#b == a
#True
######################################循环########################################
print("######################################循环########################################")
count = 0
while count < 5:
    count = count + 1
    print(count,"+++")
else:
    count = count - 1
    print(count,"---")
count=0
for var2 in "abcdefg":
    count=count+1;
    print("第",count,"个数字",var2)
#通过序列索引迭代
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index] )
count=0
count1=[1,2,3,4,5,6,7,8,9,10]
for count in count1:
    count=count+1
    if count%2==0:
        print("if",count)
    else:
        print("else1",count)
else:
    print("else2",count)
######################################日期和时间########################################
print("######################################日期和时间########################################")
ticks = time.time()
print("当前时间戳为:", ticks)
#struct_time元组
localtimes = time.localtime(time.time())
print("本地时间为 :", localtimes)
#格式化
localtime = time.asctime(time.localtime(time.time()))
print("格式化后的本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:",cal)

q1=2
q2=3
print(q2/q1)