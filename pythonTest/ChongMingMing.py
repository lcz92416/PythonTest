import os
import sys
import time
import datetime

print("---------------------------重命名文件---------------------------")
while True:
    src = ""
    while not os.path.exists(src):
        print("请输入文件目录（不加文件名表示按规则重命名整个目录下文件）：")
        src = input()
        if os.path.exists(src):
            print("原目录为：" + src)
            break
        else:
            print("不是路径，请重新输入！")
    print("请输入要规避的文件类型(多个时以|区分，不需要规避则直接Enter)：")
    ignoreType = ""
    ignoreType = input()
    print("重命名规则：")
    print("新名称直接书写")
    print("原文件名以/n，编号/r指定位数(默认4位)、日期/d、精确到秒/ds、精确到毫秒/dm")
    print("删除/del_one删除内容、/del_all删除内容")
    print("按修改日期排序/s指定位数或输入任意字符表示重命名位修改时间(需单独使用)")
    print("例：/d/|/n|/r，重命名后为：日期原名编号；"
          "/del_one删除内容，重命名后为：原名-删除内容；"
          "/del_all删除内容|/d|/n|/r3先删除，后拼接，3位数"
          "标签重复无效，以|分割")
    tagAll = ""
    while tagAll == "":
        print("请输入重命名规则：")
        tagAll = input()
    print("重命名规则：" + tagAll + " 规避的文件类型：" + ignoreType)

    flag = 1
    resultMap = {}
    pathMap = {}


    def re_name(src, tagAll):
        global resultMap
        global flag
        global pathMap
        global ignoreType
        # 判断是否是文件夹
        if os.path.isdir(src):
            if "/s" in tagAll:
                re_name_s(src, tagAll)
            else:
                pathList = os.listdir(src)
                if len(pathList) > 1 and "|" not in tagAll and "/" not in tagAll:
                    tagAll += "|/r"
                for i in range(0, len(pathList)):
                    dirpath = os.path.join(src, pathList[i])
                    re_name(dirpath, tagAll)
        else:
            # 获取文件名
            type = ""
            if src.rfind(".") != -1:
                type = src[src.rfind("."):len(src)]
            # 不需要多级重命名
            if type == "" or type == ".":
                return
            if ignoreType != "":
                ignore = ignoreType.split("|")
                if type[1:len(type)] in ignore:
                    return

            name = os.path.basename(src).split(".")[0]
            tags = tagAll.split("|")
            # 获取文件路径
            path = os.path.dirname(src) + "\\"
            result = ""
            for tag in tags:
                if "/del_one" in tag:
                    tag = tag.replace("/del_one", "", 1)
                    result += name.replace(tag, "", 1)
                elif "/del_all" in tag:
                    tag = tag.replace("/del_all", "", 1)
                    result += name.replace(tag, "")
                elif "/n" in tag:
                    result += name
                elif "/s" in tag:
                    mtime = os.stat(src).st_mtime
                    file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                    print("{0} 修改时间是: {1}".format(src, file_modify_time))
                    result += name
                elif "/r" in tag:
                    if len(tag) == 3:
                        try:
                            tag = tag[2: 3]
                            # 补零
                            result += str(flag).zfill(int(tag))
                        except (TypeError, ValueError):
                            print("/r规则输入出错，请检查后重试！")
                    else:
                        result += str(flag).zfill(4)
                elif "/d" in tag:
                    tag = tag.replace("/d", "", 1)
                    if tag == "s":
                        result += time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))
                        time.sleep(1)
                    elif tag == "m":
                        result += str(datetime.datetime.now()).replace(":", "").replace(" ", "-")
                        time.sleep(0.001)
                    else:
                        # 格式化日期
                        result += time.strftime('%Y-%m-%d', time.localtime(time.time()))
                else:
                    result += tag.replace("\\", "").replace("/", "").replace(":", "").replace("*", "") \
                        .replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
            if result == name or result == "":
                return
            pathMap.update({str(flag): src})
            resultMap.update({str(flag): path + result + type})
            flag += 1


    def re_name_s(src, tag):
        global resultMap
        global flag
        global pathMap
        global ignoreType
        list = []
        files = os.listdir(src)
        # 对files进行排序，x是files的元素，后面的是排序的依据，x只是文件名，所以要带上join
        files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(src, x)))
        for file in files:
            type = ""
            if file.rfind(".") != -1:
                type = file[file.rfind("."):len(file)]
            # 不需要多级重命名
            if type == "" or type == ".":
                continue
            if ignoreType != "":
                ignore = ignoreType.split("|")
                if type[1:len(type)] in ignore:
                    continue
            if len(tag) == 3:
                try:
                    result = str(flag).zfill(int(tag[2: 3]))
                except (TypeError, ValueError):
                    print("/r规则输入出错，请检查后重试！")
                    result = time.strftime('%Y-%m-%d %H%M%S', time.localtime(os.stat(src + "\\" + file).st_mtime))
            else:
                result = str(flag).zfill(4)
            result = src + "\\" + result
            temp = result
            i = 1
            while result in list:
                result = temp
                result += str(i)
                i += 1
            list.append(result)
            pathMap.update({str(flag): src + "\\" + file})
            resultMap.update({str(flag): result + type})
            flag += 1


    def re_name_confirm():
        global resultMap
        global pathMap
        global flag
        flag = len(resultMap)
        if flag == 0:
            print("没有需要重命名的文件")
            return
        print("将重命名成下列文件，是否确认？")
        for key, value in resultMap.items():
            print(key + ":" + pathMap[key] + "-------->" + value)
        print("请输入(Y/N)")
        confirm = input()
        if confirm.upper() == "Y":
            for key, value in resultMap.items():
                os.rename(pathMap[key], value)
        else:
            flag = 0
            return


    re_name(src, tagAll)
    re_name_confirm()
    print("重命名" + str(flag) + "个文件")
    print("退出请输入Y...")
    quitConfirm = input()
    if quitConfirm.upper() == "Y":
        sys.exit()
