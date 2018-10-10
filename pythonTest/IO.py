import os
str = input("请输入：")
print("你输入的内容是: ", str)

#文件名，打开类型，缓冲区
fo = open("foo.txt", "r+", 1024)
#读取10个的字符串
str = fo.read(10)
print(str)
# 查找当前位置
position = fo.tell()
print(position)
# 把指针再次重新定位到文件开头
#seek（offset [,from]）from=0 开头，1当前，2结尾
position = fo.seek(0, 0)
print(position)
fo.write("www.runoob.com!\nVery good site!")
print(fo.read())
#返回被打开文件的访问模式。
print(fo.mode)
fo.close()
#得到当前目录
print(os.getcwd())
#os.rename("test1.txt", "test2.txt")
#os.remove("test1.txt")
#递归删除
#os.removedirs("")
#新建目录
os.mkdir("newdir")
os.rmdir("newdir")

ret = os.access("/foo.txt", os.F_OK)
print("F_OK 测试path是否存在- 返回值 %s"% ret)
ret = os.access("/foo.txt", os.R_OK)
print("R_OK 测试path是否可读- 返回值 %s"% ret)
ret = os.access("/foo.txt", os.W_OK)
print("W_OK 测试path是否可写- 返回值 %s"% ret)
ret = os.access("/foo.txt", os.X_OK)
print("X_OK 测试path是否可执行- 返回值 %s"% ret)


try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
#raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行
    if 1 <= 1:
        raise Exception("Invalid level!")
except:# IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
finally:
    print("总会执行")

#自定义异常
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise Networkerror("Bad hostname")
except Networkerror:
    print(e.args)