import os
import time
print("---------------------------重命名文件---------------------------")
src = ""
while not os.path.exists(src):
    print("请输入文件目录（不加文件名表示按规则重命名整个目录下文件）：")
    src = input()
    if os.path.exists(src):
        print("原目录为：" + src)
        break
    else:
        print("输入的字符串不是路径，请重新输入！")
print("命名规则：")
print("1、输入的字符串将拼接到文件名开头")
print("2、含有@t@的命名将拼接至文件末尾，并不含@t@")
print("3、含有@n@的命名将在文件末尾拼接编号，并不含@n@")
print("4、含有@d@的命名将在文件末尾拼接日期，并不含@d@")
print("5、含有@delf@的命名则删除文件中包含的内容，仅第一个，并不含@delf@")
print("6、含有@dela@的命名则删除文件中包含的内容，并不含@dela@")
print("请输入重命名规则：")
tag = input()
print("重命名规则：" + tag)

flag=1
def reName(src,tag):
    # 判断是否是文件夹
    if os.path.isdir(src):
        list = os.listdir(src)
        for i in range(0,len(list)):
            dirpath = os.path.join(src,list[i])
            reName(dirpath,tag)
    else:
        global flag
        print(str(flag)+"："+src+"-------->",end="")
        #获取文件名
        name=os.path.basename(src).split(".")[0]
        type=""
        if src.rfind(".")!=-1:
            type=src[src.rfind("."):len(src)]
        #获取文件路径
        path=os.path.dirname(src)+"\\"
        if "@delf@" in tag:
            tag=tag.replace("@delf@","",1)
            name=name.replace(tag,"",1)
            os.rename(src,path+name+type)
            print(path+name+type)
        elif "@dela@" in tag:
            tag=tag.replace("@dela@","",1)
            name=name.replace(tag,"")
            os.rename(src,path+name+type)
            print(path+name+type)
        elif "@t@" in tag:
            tag=tag.replace("@t@","",1)
            os.rename(src,path+name+tag+type)
            print(path+name+tag+type)
        elif "@n@" in tag:
            tag=tag.replace("@n@","",1)
            #补零
            tag=tag+str(flag).zfill(5)
            os.rename(src,path+name+tag+type)
            print(path+name+tag+type)
        elif "@d@" in tag:
            tag=tag.replace("@d@","",1)
            #格式化日期
            tag=tag+" "+time.strftime('%Y-%m-%d',time.localtime(time.time()))
            os.rename(src,path+name+tag+type)
            print(path+name+tag+type)
        else:
            os.rename(src,path+tag+name+type)
            print(path+tag+name+type)
        flag+=1
reName(src,tag)
print("重命名完成，共" + str(flag)+"个文件")
input("请按回车键退出...")


