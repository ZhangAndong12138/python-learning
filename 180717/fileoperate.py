
import os
import shutil


def copyfile(source, target):
    print("正在把文件复制到路径:["+target+"],稍候...")
    shutil.copytree(source, target)
    print("文件复制完成!")


def replace_xml(path):
    if(path.endswith(".xml")):
        f = open(path, "r", encoding="UTF-8")
        filecontent = ""
        line = f.readline()
        while line:
            temp_line = line.replace("127.0.0.1:8080", "192.168.101.18:7001")
            temp_line = temp_line.replace("localhost:8080", "192.168.101.18:7001")
            filecontent += temp_line
            line = f.readline()
        f.close()
        f = open(path, "w", encoding="UTF-8")
        f.writelines(filecontent)
        f.close()


def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            replace_xml(tmp_path)
        else:
            traverse(tmp_path)
