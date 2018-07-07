# zip a file

import zipfile
import glob
import os

target_path = "E:/target/"
files = glob.glob(target_path + "*")
f = zipfile.ZipFile("crew.zip", "w", zipfile.ZIP_DEFLATED)

for file in files:
    f.write(file, "E:/" + os.path.basename(file))

f.close()
