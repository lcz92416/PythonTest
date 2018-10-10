# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    #自动获取编码
    charset = chardet.detect(html)
    print(charset)
    html = html.decode("utf-8")
    # print(html)

