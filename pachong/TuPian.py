from urllib import request
from bs4 import BeautifulSoup
import os
url = "https://www.mygalgame.com"
print(url+"图片保存程序启动...")
print("图片保存程序启动...")
html = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())

#用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
links = soup.find_all("style")
print(links)
urls=str(links[0]).split("background-image: url(")
# 设置保存图片的路径，否则会保存到程序当前路径
path = r'F:\python\images'                            #路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义
try:
    flag=0
    for url in urls:
        if(".jpg" in url):
            u=url.split(");}")
            #保存链接并命名，time.time()返回当前时间戳防止命名冲突
            p=u[0];
            s=p[p.rfind("/"):len(p)]
            print("第"+str(flag)+"个图片保存中...")
            print(p+"---"+s)
            request.urlretrieve(p,path+'\%s' % s)
            flag+=1
    print("已成功保存"+str(flag)+"张图片！")
except:
    print("图片保存失败！")
    for url in urls:
        if(".jpg" in url):
            u=url.split(");}")
            p=u[0];
            s=p[p.rfind("/"):len(p)]
            print(p+"---"+s)
            os.remove(path+'\%s' % s)
finally:
    input("请按回车键退出...")

