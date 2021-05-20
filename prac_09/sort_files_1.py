import os
import shutil

os.chdir('FilesToSort')
for directory, subdirectories, filenames in os.walk("."):
    for file in filenames:
        sub_name = file.split(".")[1]
        try:
            os.mkdir(sub_name)
        except FileExistsError:
            pass
        shutil.move(file, "{}/".format(sub_name))
