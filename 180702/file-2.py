# file test
# 1:copy a file to another path
# 2:replace some string

import os
import shutil
from datetime import datetime

os.chdir("E:/faban")

filename = datetime.now().strftime("%y%m%d")

shutil.copytree("E:/cvicse/crew_dce/WebRoot/ewm", "E:/faban/"+filename)
print("files are copied to path:["+filename+"] !")
