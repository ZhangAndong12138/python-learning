# file test
# 1:copy a file to another path
# 2:replace some string

import os
import shutil
from datetime import datetime

source_path = "F:/crewDev/out/artifacts"
target_path = "F:/faban/"

os.chdir(target_path)

floder_name = datetime.now().strftime("%y%m%d%H%M")

print("files are copying to path:["+floder_name+"],pleasewait...")
shutil.copytree(source_path, target_path+floder_name)
print("files were copied to path:["+floder_name+"] !")
