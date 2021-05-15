import os
import shutil

os.chdir('FilesToSort')
for directory, subdirectories, filenames in os.walk("."):
    sub_reference = {}
    check = []
    for file in filenames:
        file_type = file.split(".")[1]
        if file_type not in check:
            sub_name = input("What category would you like to sort {} files into? ".format(file_type))
            if sub_name in sub_reference.keys():
                sub_reference[sub_name].append(file_type)
            else:
                sub_reference[sub_name] = [file_type]
                os.mkdir(sub_name)
            print(sub_reference)
            check.append(file_type)
