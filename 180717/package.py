import os
import fileoperate as f
from datetime import datetime

source_path = "E:/source/"
target_path = "E:/target/"

os.chdir(target_path)

floder_name = datetime.now().strftime("%y%m%d%H%M")

f.copyfile(source_path, target_path+floder_name)

os.chdir(target_path+floder_name)

f.traverse(target_path+floder_name)

