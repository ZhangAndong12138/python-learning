# replace str in file


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


path = "E:/target/1807031512/dce/WEB-INF/classes/client-declare-person-beans.xml"
replace_xml(path)
