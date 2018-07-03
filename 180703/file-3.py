# file test
# 1:copy a file to another path
# ->2:replace some string

import os
import shutil
from datetime import datetime

source_path = "E:/source/"
target_path = "E:/target/"

os.chdir(target_path)

floder_name = datetime.now().strftime("%y%m%d%H%M")

print("files are copying to path:["+floder_name+"],pleasewait...")
shutil.copytree(source_path, target_path+floder_name)
print("files were copied to path:["+floder_name+"] !")

os.chdir(target_path+floder_name)


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


traverse(target_path+floder_name)
